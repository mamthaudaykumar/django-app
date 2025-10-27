from django.db import models

class Book(models.Model):
    book_id = models.IntegerField(unique=True)
    isbn = models.CharField(max_length=20)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "books"

    def __str__(self):
        return f"{self.title} by {self.author}"
