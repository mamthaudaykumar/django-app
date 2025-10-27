from django.urls import path
from .views_generated import *

urlpatterns = [
    path('api/v1/book/', GetAllBooksApiV1BookGetView.as_view()),
    path('api/v1/book/', CreatebooksView.as_view()),
    path('api/v1/book/{book_id}', UpdateBookApiV1BookBookIdPutView.as_view()),
    path('api/v1/book/{book_id}', GetBookApiV1BookBookIdGetView.as_view()),
    path('api/v1/book/bookstatus/update', UpdateBookStatusView.as_view()),
    path('api/v1/book/books/search', SearchBooksApiV1BookBooksSearchGetView.as_view()),
    path('api/v1/book/report/rented-books', GetrentedbooksreportView.as_view()),
    path('api/v1/user/{user_id}/book/{book_id}/wishlist', AddtowishlistView.as_view()),
    path('api/v1/user/{user_id}/book/{book_id}/wishlist', RemovefromwishlistView.as_view()),
    path('api/v1/user/{user_id}/wishlist', ListwishlistView.as_view()),
    path('', HealthGetView.as_view()),
]