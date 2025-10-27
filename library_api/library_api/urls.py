from django.contrib import admin
from django.urls import path, include
from user_app.urls.urls_generated_user_app_user import urlpatterns as user_app_user_urls
from books_app.urls.urls_generated_books_app_book import urlpatterns as books_app_book_urls


from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('user_app_user/', include(user_app_user_urls)),
    path('books_app_book/', include(books_app_book_urls)),
    path('admin/', admin.site.urls),
    # Schema & Swagger UI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
