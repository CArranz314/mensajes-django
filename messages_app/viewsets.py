from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from .serializers import MessageSerializer
from .models import Message, User
from .pagination import SmallSetPagination


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return super().get_queryset()


class UserViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return super().get_queryset()


class MessageAPIViewSet(APIView):
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


class MessagesPerUserAPIViewSet(APIView):
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
