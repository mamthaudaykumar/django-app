from django.contrib import admin
from django.urls import path, include
from book.urls.urls_generated_book_book import urlpatterns as book_book_urls
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('book_book/', include(book_book_urls)),
    path('admin/', admin.site.urls),
    # Schema & Swagger UI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
