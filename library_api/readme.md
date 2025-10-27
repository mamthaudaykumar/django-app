# Django openapi generator from yaml
1. Add [generate_django_from_openapi.py](generate_from_openapi.py)
2. Run command: python generate_django_from_openapi.py
3. Include generated URLs in your project. 
 
   from django.urls import include, path
       urlpatterns = [
           path("api/v1/", include("books.urls_generated")),
       ]
4. python manage.py runserver. Access swagger - http://localhost:8000/api/schema/swagger-ui/



openapi-generator-cli generate \
  -i book.yaml \
  -g python \
  -o ./generated_python


openapi-generator-cli generate \
  -i book.yaml \
  -g python-pydantic-v1 \
  -o ./generated_models


python generate_from_openapi.py --app books_app --yaml api/book.yaml --project library_api

# Generate app from OpenAPI YAML
python generate_from_openapi.py --app books_app --yaml api/book.yaml --project library_api

# Delete app completely
python generate_from_openapi.py --app books_app --yaml api/book.yaml --project library_api --delete-app
