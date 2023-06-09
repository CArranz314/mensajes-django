from rest_framework import serializers

from .models import Message

from django.contrib.auth.models import User


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Message objects
    """

    class Meta:
        model = Message
        fields = ["id", "title", "content", "user", "date"]


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User objects
    """

    class Meta:
        model = User
        fields = ["username", "email", "is_staff"]
