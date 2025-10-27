from rest_framework import serializers


class BookRequestSerializer(serializers.Serializer):
    book_id = serializers.IntegerField(required=True)
    isbn = serializers.CharField(required=True)
    author = serializers.CharField(required=True)
    publication_year = serializers.IntegerField(required=True)
    title = serializers.CharField(required=True)
    language = serializers.CharField(required=True)


class BookResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    book_id = serializers.IntegerField(required=True)
    isbn = serializers.CharField(required=True)
    author = serializers.CharField(required=True)
    publication_year = serializers.CharField(required=False)
    title = serializers.CharField(required=True)
    language = serializers.CharField(required=False)
    status_details = serializers.CharField(required=False)


class BookCreateResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    book_id = serializers.IntegerField(required=True)
    isbn = serializers.CharField(required=True)
    author = serializers.CharField(required=True)
    publication_year = serializers.CharField(required=False)
    title = serializers.CharField(required=True)
    language = serializers.CharField(required=False)


class BookUpdateResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    book_id = serializers.IntegerField(required=True)
    isbn = serializers.CharField(required=True)
    author = serializers.CharField(required=True)
    publication_year = serializers.CharField(required=False)
    title = serializers.CharField(required=True)
    language = serializers.CharField(required=False)


class BookBorrowStatusRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    book_id = serializers.IntegerField(required=True)
    status = serializers.CharField(required=True)


class StatusDetailsSerializer(serializers.Serializer):
    status = serializers.CharField(required=True)
    borrowerId = serializers.CharField(required=False)
    borrowerName = serializers.CharField(required=False)
    borrowedOn = serializers.CharField(required=False)


class HTTPValidationErrorSerializer(serializers.Serializer):
    detail = serializers.ListField(required=False)


class ValidationErrorSerializer(serializers.Serializer):
    loc = serializers.ListField(required=True)
    msg = serializers.CharField(required=True)
    type = serializers.CharField(required=True)
