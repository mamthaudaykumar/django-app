import yaml
from pathlib import Path

spec_path = Path("./api/api_spec.yaml")
output_dir = Path("books")
views_file = output_dir / "views_generated.py"
serializers_file = output_dir / "serializers_generated.py"
urls_file = output_dir / "urls_generated.py"

spec = yaml.safe_load(spec_path.read_text())

views = []
urls = []

for path, methods in spec.get("paths", {}).items():
    for method, details in methods.items():
        operation_id = details.get("operationId", f"{method}_{path}")
        summary = details.get("summary", "")
        name = operation_id.replace("-", "_")

        # Controller stub
        view_class = f"""
class {name.title().replace("_", "")}View(APIView):
    \"\"\"{summary}\"\"\"
    def {method}(self, request, *args, **kwargs):
        # TODO: implement controller logic for {path}
        return Response({{"message": "Not implemented"}}, status=501)
"""
        views.append(view_class)

        # URL stub
        urls.append(f"path('{path.lstrip('/')}', {name.title().replace('_', '')}View.as_view()),")

views_code = """from rest_framework.views import APIView
from rest_framework.response import Response

""" + "\n".join(views)

urls_code = """from django.urls import path
from .views_generated import *

urlpatterns = [
""" + "\n".join(["    " + u for u in urls]) + "\n]"

views_file.write_text(views_code)
urls_file.write_text(urls_code)
print("Generated DRF view + URL stubs from OpenAPI spec!")
