from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.serializers_generated_api_user import *


class AddToWishlistBaseView(APIView):
    """Add a book to wishlist"""
    def post(self, request, *args, **kwargs):
        # TODO: implement logic for /user/{user_id}/book/{book_id}/wishlist
        return Response({"message": "Not implemented"}, status=501)


class RemoveFromWishlistBaseView(APIView):
    """Remove a book from wishlist"""
    def delete(self, request, *args, **kwargs):
        # TODO: implement logic for /user/{user_id}/book/{book_id}/wishlist
        return Response({"message": "Not implemented"}, status=501)


class ListWishlistBaseView(APIView):
    """List a user's wishlist"""
    def get(self, request, *args, **kwargs):
        # TODO: implement logic for /user/{user_id}/wishlist
        return Response({"message": "Not implemented"}, status=501)
