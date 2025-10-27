from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.serializers_generated_api_book import *


class GetAllBooksBaseView(APIView):
    """Get All Books"""
    def get(self, request, *args, **kwargs):
        # TODO: implement logic for /book/
        return Response({"message": "Not implemented"}, status=501)


class CreateBooksBaseView(APIView):
    """Create books"""
    def post(self, request, *args, **kwargs):
        # TODO: implement logic for /book/
        return Response({"message": "Not implemented"}, status=501)


class GetBookBaseView(APIView):
    """Get Book"""
    def get(self, request, *args, **kwargs):
        # TODO: implement logic for /book/{book_id}
        return Response({"message": "Not implemented"}, status=501)


class UpdateBookBaseView(APIView):
    """Update Book"""
    def put(self, request, *args, **kwargs):
        # TODO: implement logic for /book/{book_id}
        return Response({"message": "Not implemented"}, status=501)


class UpdateBookStatusBaseView(APIView):
    """Update book status"""
    def put(self, request, *args, **kwargs):
        # TODO: implement logic for /book/bookstatus/update
        return Response({"message": "Not implemented"}, status=501)


class SearchBooksBaseView(APIView):
    """Search books by author and/or title"""
    def get(self, request, *args, **kwargs):
        # TODO: implement logic for /book/books/search
        return Response({"message": "Not implemented"}, status=501)


class GetRentedBooksReportBaseView(APIView):
    """Get report of currently rented books"""
    def get(self, request, *args, **kwargs):
        # TODO: implement logic for /book/report/rented-books
        return Response({"message": "Not implemented"}, status=501)


class HealthBaseView(APIView):
    """Health"""
    def get(self, request, *args, **kwargs):
        # TODO: implement logic for /
        return Response({"message": "Not implemented"}, status=501)
