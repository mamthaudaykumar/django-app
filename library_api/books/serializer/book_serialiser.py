from rest_framework import serializers
from books.models.book import Book
from books.models.book_borrow import BookBorrowStatus


class StatusDetailsSerializer(serializers.Serializer):
    status = serializers.CharField()
    borrowerId = serializers.IntegerField(required=False, allow_null=True)
    borrowerName = serializers.CharField(required=False, allow_null=True)
    borrowedOn = serializers.DateTimeField(required=False, allow_null=True)

class BookSerializer(serializers.ModelSerializer):
    status_details = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'book_id', 'isbn', 'author', 'publication_year', 'title', 'language', 'status_details']

    def get_status_details(self, obj):
        borrow = BookBorrowStatus.objects.filter(book=obj, status='BORROWED').first()
        if borrow:
            return {
                "status": borrow.status,
                "borrowerId": borrow.user.id,
                "borrowerName": borrow.user.name,
                "borrowedOn": borrow.borrowed_on
            }
        return None
