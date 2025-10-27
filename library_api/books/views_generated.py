from rest_framework.views import APIView
from rest_framework.response import Response


class GetAllBooksApiV1BookGetView(APIView):
    """Get All Books"""
    def get(self, request, *args, **kwargs):
        # TODO: implement controller logic for /api/v1/book/
        return Response({"message": "Not implemented"}, status=501)


class CreatebooksView(APIView):
    """Create books"""
    def post(self, request, *args, **kwargs):
        # TODO: implement controller logic for /api/v1/book/
        return Response({"message": "Not implemented"}, status=501)


class UpdateBookApiV1BookBookIdPutView(APIView):
    """Update Book"""
    def put(self, request, *args, **kwargs):
        # TODO: implement controller logic for /api/v1/book/{book_id}
        return Response({"message": "Not implemented"}, status=501)


class GetBookApiV1BookBookIdGetView(APIView):
    """Get Book"""
    def get(self, request, *args, **kwargs):
        # TODO: implement controller logic for /api/v1/book/{book_id}
        return Response({"message": "Not implemented"}, status=501)


class UpdateBookStatusView(APIView):
    """Update book status"""
    def put(self, request, *args, **kwargs):
        # TODO: implement controller logic for /api/v1/book/bookstatus/update
        return Response({"message": "Not implemented"}, status=501)


class SearchBooksApiV1BookBooksSearchGetView(APIView):
    """Search books by author and/or title"""
    def get(self, request, *args, **kwargs):
        # TODO: implement controller logic for /api/v1/book/books/search
        return Response({"message": "Not implemented"}, status=501)


class GetrentedbooksreportView(APIView):
    """Get report of currently rented books and rental duration"""
    def get(self, request, *args, **kwargs):
        # TODO: implement controller logic for /api/v1/book/report/rented-books
        return Response({"message": "Not implemented"}, status=501)


class AddtowishlistView(APIView):
    """Add a book to wishlist"""
    def post(self, request, *args, **kwargs):
        # TODO: implement controller logic for /api/v1/user/{user_id}/book/{book_id}/wishlist
        return Response({"message": "Not implemented"}, status=501)


class RemovefromwishlistView(APIView):
    """Remove a book from wishlist"""
    def delete(self, request, *args, **kwargs):
        # TODO: implement controller logic for /api/v1/user/{user_id}/book/{book_id}/wishlist
        return Response({"message": "Not implemented"}, status=501)


class ListwishlistView(APIView):
    """List a user's wishlist"""
    def get(self, request, *args, **kwargs):
        # TODO: implement controller logic for /api/v1/user/{user_id}/wishlist
        return Response({"message": "Not implemented"}, status=501)


class HealthGetView(APIView):
    """Health"""
    def get(self, request, *args, **kwargs):
        # TODO: implement controller logic for /
        return Response({"message": "Not implemented"}, status=501)
