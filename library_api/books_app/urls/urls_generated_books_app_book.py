from django.urls import path
from ..views.views_generated_books_app_book import *

urlpatterns = [
    path('book/', GetAllBooksBaseView.as_view()),
    path('book/', CreateBooksBaseView.as_view()),
    path('book/{book_id}', GetBookBaseView.as_view()),
    path('book/{book_id}', UpdateBookBaseView.as_view()),
    path('book/bookstatus/update', UpdateBookStatusBaseView.as_view()),
    path('book/books/search', SearchBooksBaseView.as_view()),
    path('book/report/rented-books', GetRentedBooksReportBaseView.as_view()),
    path('', HealthBaseView.as_view()),]
