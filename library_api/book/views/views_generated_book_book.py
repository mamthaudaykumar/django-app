from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import serializers_generated_book_book


class GetAllBooksBaseView(APIView):
    """Get All Books"""
    def get(self, request, *args, **kwargs):
        return Response({"message": "Not implemented"}, status=501)


class CreateBooksBaseView(APIView):
    """Create books"""
    def post(self, request, *args, **kwargs):
        return Response({"message": "Not implemented"}, status=501)


class GetBookBaseView(APIView):
    """Get Book"""
    def get(self, request, *args, **kwargs):
        return Response({"message": "Not implemented"}, status=501)


class UpdateBookBaseView(APIView):
    """Update Book"""
    def put(self, request, *args, **kwargs):
        return Response({"message": "Not implemented"}, status=501)


class UpdateBookStatusBaseView(APIView):
    """Update book status"""
    def put(self, request, *args, **kwargs):
        return Response({"message": "Not implemented"}, status=501)


class SearchBooksBaseView(APIView):
    """Search books by author and/or title"""
    def get(self, request, *args, **kwargs):
        return Response({"message": "Not implemented"}, status=501)


class GetRentedBooksReportBaseView(APIView):
    """Get report of currently rented books"""
    def get(self, request, *args, **kwargs):
        return Response({"message": "Not implemented"}, status=501)


class HealthBaseView(APIView):
    """Health"""
    def get(self, request, *args, **kwargs):
        return Response({"message": "Not implemented"}, status=501)
