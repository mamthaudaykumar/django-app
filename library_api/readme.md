# Django openapi generator from yaml
1. Add [generate_django_from_openapi.py](generate_django_from_openapi.py)
2. Run command: python generate_django_from_openapi.py
3. Include generated URLs in your project. 
 
   from django.urls import include, path
       urlpatterns = [
           path("api/v1/", include("books.urls_generated")),
       ]
4. python manage.py runserver. Access swagger - http://localhost:8000/api/schema/swagger-ui/
