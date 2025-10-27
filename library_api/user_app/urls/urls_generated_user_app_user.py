from django.urls import path
from ..views.views_generated_user_app_user import *

urlpatterns = [
    path('user/{user_id}/book/{book_id}/wishlist', AddToWishlistBaseView.as_view()),
    path('user/{user_id}/book/{book_id}/wishlist', RemoveFromWishlistBaseView.as_view()),
    path('user/{user_id}/wishlist', ListWishlistBaseView.as_view()),]
