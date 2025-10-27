from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import serializers_generated_user_app_user


class AddToWishlistBaseView(APIView):
    """Add a book to wishlist"""
    def post(self, request, *args, **kwargs):
        return Response({"message": "Not implemented"}, status=501)


class RemoveFromWishlistBaseView(APIView):
    """Remove a book from wishlist"""
    def delete(self, request, *args, **kwargs):
        return Response({"message": "Not implemented"}, status=501)


class ListWishlistBaseView(APIView):
    """List a user's wishlist"""
    def get(self, request, *args, **kwargs):
        return Response({"message": "Not implemented"}, status=501)
