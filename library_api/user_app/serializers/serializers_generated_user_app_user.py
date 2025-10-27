from rest_framework import serializers


class WishlistItemResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    user_id = serializers.IntegerField(required=True)
    book_id = serializers.IntegerField(required=True)


class HTTPValidationErrorSerializer(serializers.Serializer):
    detail = serializers.ListField(required=False)


class ValidationErrorSerializer(serializers.Serializer):
    loc = serializers.ListField(required=True)
    msg = serializers.CharField(required=True)
    type = serializers.CharField(required=True)
