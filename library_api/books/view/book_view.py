from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from books.dao.book_dao import BookDAO
from books.serializers.book_serializers import BookSerializer

class BookListCreateView(APIView):

    def get(self, request):
        books = BookDAO.get_all_books()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = BookDAO.create_book(**serializer.validated_data)
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(APIView):

    def get(self, request, book_id):
        book = BookDAO.get_book_by_id(book_id)
        if not book:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, book_id):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = BookDAO.update_book(book_id, **serializer.validated_data)
            return Response(BookSerializer(book).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
