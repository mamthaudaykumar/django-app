# models/borrow_status.py
from django.db import models

class BookBorrowStatus(models.Model):
    STATUS_CHOICES = [
        ('BORROWED', 'Borrowed'),
        ('RETURNED', 'Returned'),
        ('LOST', 'Lost'),
    ]

    user = models.ForeignKey("books.UsersDetails", on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    borrowed_on = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_book_borrow_details"

    def __str__(self):
        return f"{self.user} - {self.book} ({self.status})"
