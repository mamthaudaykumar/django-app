from django.db import models

from .book import Book
from .user_detail import UsersDetails


class UserBookWishlist(models.Model):
    user = models.ForeignKey(UsersDetails, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_wishlist"
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user.name} → {self.book.title}"
