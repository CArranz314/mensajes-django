from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from .serializers import MessageSerializer, UserSerializer
from .models import Message, User
from .pagination import SmallSetPagination


class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Message object requests (extends ModelViewSet)
    """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return super().get_queryset()

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class MessagePostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Message object POST requests (extends ModelViewSet)
    """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = [
        "post",
    ]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User object requests (extends ModelViewSet)
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return super().get_queryset()


class MessageAPIView(APIView):
    """
    API view for Message object requests (extends APIView)
    """

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Message.objects.all().exists():
            messages = Message.objects.all()
            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(messages, request)
            serializer = MessageSerializer(results, many=True)

            return paginator.get_paginated_response({"messages": serializer.data})
        else:
            return Response(
                {"error": "404 not found"}, status=status.HTTP_404_NOT_FOUND
            )


class MessagesPerUserAPIView(APIView):
    """
    API view for User object requests (extends APIView)
    """

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Message.objects.all().exists():
            user_pk = request.query_params.get("user")
            user = get_object_or_404(User, pk=user_pk)

            messages = Message.objects.all().filter(user=user)
            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(messages, request)
            serializer = MessageSerializer(results, many=True)

            return paginator.get_paginated_response(
                {"messages by " + user.username: serializer.data}
            )
        else:
            return Response(
                {"error": "404 not found"}, status=status.HTTP_404_NOT_FOUND
            )
