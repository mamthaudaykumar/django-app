from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from books.models.book_wishlist import UserBookWishlist


class WishlistView(APIView):

    def get(self, request, user_id):
        items = UserBookWishlist.objects.filter(user_id=user_id)
        data = [{"id": i.id, "user_id": i.user.id, "book_id": i.book.id} for i in items]
        return Response(data)

    def post(self, request, user_id, book_id):
        obj, created = UserBookWishlist.objects.get_or_create(user_id=user_id, book_id=book_id)
        if created:
            return Response({"message": "Book added to wishlist"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Already in wishlist"}, status=status.HTTP_200_OK)

    def delete(self, request, user_id, book_id):
        UserBookWishlist.objects.filter(user_id=user_id, book_id=book_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
