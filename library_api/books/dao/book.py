from books.models.book import Book
from books.models.book_borrow import BookBorrowStatus


class BookDAO:

    @staticmethod
    def get_all_books():
        return Book.objects.all()

    @staticmethod
    def get_book_by_id(book_id):
        return Book.objects.filter(id=book_id).first()

    @staticmethod
    def create_book(**kwargs):
        return Book.objects.create(**kwargs)

    @staticmethod
    def update_book(book_id, **kwargs):
        Book.objects.filter(id=book_id).update(**kwargs)
        return Book.objects.get(id=book_id)

    @staticmethod
    def update_book_status(book_id, user_id, status):
        borrow, _ = BookBorrowStatus.objects.get_or_create(book_id=book_id, user_id=user_id)
        borrow.status = status
        borrow.save()
        return borrow
