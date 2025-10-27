import subprocess
import yaml
from pathlib import Path
import re
import argparse
import shutil
import sys

# -----------------------------
# Helpers
# -----------------------------
def write_file_if_missing(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        print(f"⏩ Skipping existing file {path}")
    else:
        path.write_text(content)
        print(f"✅ Generated {path}")

def run_command(cmd, cwd=None):
    """Run a system command safely."""
    print(f"⚙️  Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True, cwd=cwd)

# -----------------------------
# Run OpenAPI Generator CLI
# -----------------------------
def run_openapi_generator(spec_path: Path):
    print(f"\n🚀 Running OpenAPI Generator for {spec_path}")
    run_command([
        "openapi-generator-cli", "generate",
        "-i", str(spec_path),
        "-g", "python",
        "-o", "./generated_python",
        "--skip-validate-spec"
    ])
    run_command([
        "openapi-generator-cli", "generate",
        "-i", str(spec_path),
        "-g", "python-pydantic-v1",
        "-o", "./generated_models",
        "--skip-validate-spec"
    ])

# -----------------------------
# Add / Remove app from settings
# -----------------------------
def add_app_to_settings(settings_file: Path, app_name: str):
    if not settings_file.exists():
        print(f"❌ Settings file {settings_file} not found")
        return

    content = settings_file.read_text()
    pattern = r"INSTALLED_APPS\s*=\s*\[(.*?)\]"
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print("❌ Could not find INSTALLED_APPS in settings.py")
        return

    installed_apps = match.group(1)
    if f"'{app_name}'" in installed_apps or f'"{app_name}"' in installed_apps:
        print(f"⏩ App {app_name} already in INSTALLED_APPS")
        return

    new_installed_apps = installed_apps + f"\n    '{app_name}',"
    new_content = content[:match.start(1)] + new_installed_apps + content[match.end(1):]
    settings_file.write_text(new_content)
    print(f"✅ Added {app_name} to INSTALLED_APPS in {settings_file}")

def remove_app_from_settings(settings_file: Path, app_name: str):
    if not settings_file.exists():
        return
    content = settings_file.read_text()
    new_content = re.sub(rf"[\'\"]{app_name}[\'\"],?\n?", "", content)
    settings_file.write_text(new_content)
    print(f"🗑️  Removed {app_name} from INSTALLED_APPS in {settings_file}")

# -----------------------------
# Auto-include helper
# -----------------------------
def ensure_import_and_include(project_dir: Path, app_name: str, url_module: str, prefix: str, remove=False):
    """Add or remove URLs from main urls.py."""
    main_urls_file = project_dir / "urls.py"
    if not main_urls_file.exists():
        return

    code = main_urls_file.read_text()
    import_stmt = f"from {app_name}.urls.{url_module} import urlpatterns as {prefix}_urls"
    include_stmt = f"    path('{prefix}/', include({prefix}_urls)),"

    if remove:
        code = code.replace(import_stmt, "")
        code = code.replace(include_stmt, "")
        main_urls_file.write_text(code)
        print(f"🗑️  Removed URL registrations for {app_name} from {main_urls_file}")
    else:
        changed = False
        if import_stmt not in code:
            code = re.sub(r"(from django\.urls import .+)", r"\1\n" + import_stmt, code)
            changed = True
        if include_stmt not in code:
            code = re.sub(r"(urlpatterns\s*=\s*\[)", r"\1\n" + include_stmt, code)
            changed = True
        if changed:
            main_urls_file.write_text(code)
            print(f"✅ Updated {main_urls_file}")

# -----------------------------
# Main code generation
# -----------------------------
def generate_for_spec(project_dir: Path, app_name: str, spec_file: Path):
    if not spec_file.exists():
        print(f"❌ Spec file not found: {spec_file}")
        sys.exit(1)

    print(f"\n📘 Processing {spec_file} → app: {app_name}")

    # Create app if missing
    app_dir = Path(app_name)
    if not app_dir.exists():
        print(f"🪄 Creating Django app: {app_name}")
        run_command(["python", "manage.py", "startapp", app_name], cwd=project_dir)
    else:
        print(f"⏩ App {app_name} already exists")

    # Add app to settings
    settings_file = project_dir / "settings.py"
    add_app_to_settings(settings_file, app_name)

    # Run OpenAPI generator
    run_openapi_generator(spec_file)

    # Load YAML spec
    spec = yaml.safe_load(spec_file.read_text())
    spec_id = f"{app_name}_{spec_file.stem}"

    # -----------------------------
    # Create packages
    serializers_dir = app_dir / "serializers"
    views_dir = app_dir / "views"
    urls_dir = app_dir / "urls"

    for d in [serializers_dir, views_dir, urls_dir]:
        d.mkdir(parents=True, exist_ok=True)
        init_file = d / "__init__.py"
        if not init_file.exists():
            init_file.write_text("# Package init")

    serializers_file = serializers_dir / f"serializers_generated_{spec_id}.py"
    views_file = views_dir / f"views_generated_{spec_id}.py"
    urls_file = urls_dir / f"urls_generated_{spec_id}.py"

    serializers, views, urls = [], [], []

    # -----------------------------
    # 1️⃣ Generate serializers
    schemas = spec.get("components", {}).get("schemas", {})
    for schema_name, schema in schemas.items():
        fields = []
        required = schema.get("required", [])
        properties = schema.get("properties", {})

        for prop_name, prop_spec in properties.items():
            typ = prop_spec.get("type", "string")
            field_map = {
                "integer": "IntegerField",
                "string": "CharField",
                "boolean": "BooleanField",
                "array": "ListField",
                "object": "DictField",
            }
            field_type = field_map.get(typ, "CharField")
            required_flag = prop_name in required
            fields.append(f"    {prop_name} = serializers.{field_type}(required={required_flag})")

        serializer_class = f"""
class {schema_name}Serializer(serializers.Serializer):
{chr(10).join(fields) if fields else '    pass'}
"""
        serializers.append(serializer_class)

    serializers_code = """from rest_framework import serializers

""" + "\n".join(serializers)
    write_file_if_missing(serializers_file, serializers_code)

    # -----------------------------
    # 2️⃣ Generate views & URLs
    for path, methods in spec.get("paths", {}).items():
        for method, details in methods.items():
            operation_id = details.get("operationId", f"{method}_{path.strip('/')}")
            summary = details.get("summary", "")
            name = operation_id.replace("-", "_")
            class_name = f"{name.title().replace('_', '')}BaseView"
            django_path = path.lstrip("/")

            view_class = f"""
class {class_name}(APIView):
    \"\"\"{summary}\"\"\"
    def {method}(self, request, *args, **kwargs):
        # TODO: implement logic for {path}
        return Response({{"message": "Not implemented"}}, status=501)
"""
            views.append(view_class)
            urls.append(f"path('{django_path}', {class_name}.as_view()),")

    views_code = f"""from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import serializers_generated_{spec_id}

""" + "\n".join(views)
    write_file_if_missing(views_file, views_code)

    urls_code = f"""from django.urls import path
from ..views import views_generated_{spec_id}

urlpatterns = [
""" + "\n".join(["    " + u for u in urls]) + "\n]"
    write_file_if_missing(urls_file, urls_code)

    # -----------------------------
    # 3️⃣ Auto-register in main urls.py
    ensure_import_and_include(project_dir, app_name, f"urls_generated_{spec_id}", spec_id)

    print(f"🎉 Done generating code for {app_name} ({spec_file})")

# -----------------------------
# Delete app
# -----------------------------
def delete_app(project_dir: Path, app_name: str, spec_file: Path):
    app_dir = Path(app_name)
    if app_dir.exists():
        shutil.rmtree(app_dir)
        print(f"🗑️  Deleted app folder {app_dir}")

    # Remove from INSTALLED_APPS
    settings_file = project_dir / "settings.py"
    remove_app_from_settings(settings_file, app_name)

    # Remove URLs
    spec_id = f"{app_name}_{spec_file.stem}"
    ensure_import_and_include(project_dir, app_name, f"urls_generated_{spec_id}", spec_id, remove=True)

# -----------------------------
# CLI Entry Point
# -----------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate or delete Django app code from OpenAPI YAML.")
    parser.add_argument("--app", required=True, help="Django app name to create/use")
    parser.add_argument("--yaml", required=True, help="Path to the OpenAPI YAML file")
    parser.add_argument("--project", required=True, help="Main Django project folder name")
    parser.add_argument("--delete-app", action="store_true", help="Delete the app and all generated code")
    args = parser.parse_args()

    project_dir = Path(args.project)
    spec_path = Path(args.yaml)

    if args.delete_app:
        delete_app(project_dir, args.app, spec_path)
        print(f"🗑️  Deleted {args.app} and cleaned up references.")
    else:
        generate_for_spec(project_dir, args.app, spec_path)
