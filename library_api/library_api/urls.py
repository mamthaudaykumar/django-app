from django.urls import path

from books.view.book_view import BookListCreateView, BookDetailView
from books.view.wishlist_view import WishlistView

urlpatterns = [
    path('api/v1/book/', BookListCreateView.as_view(), name='book-list-create'),
    path('api/v1/book/<int:book_id>/', BookDetailView.as_view(), name='book-detail'),
    path('api/v1/user/<int:user_id>/wishlist/', WishlistView.as_view(), name='wishlist-list'),
    path('api/v1/user/<int:user_id>/book/<int:book_id>/wishlist/', WishlistView.as_view(), name='wishlist-add-remove'),
]
