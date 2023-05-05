from django.urls import path

from django.contrib.auth import views as auth_views

from .forms import LoginAccount
from . import views, viewsets


app_name = "messages_app"
urlpatterns = [
    path("", views.list, name="list"),
    path("<int:pk>", views.message_detail, name="message_detail"),
    path("new/", views.new_message, name="new_message"),
    path("create_account/", views.create_account, name="create_account"),
    # django auth views URLs
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="messages_app:list"),
        name="logout",
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="messages_app/login.html", authentication_form=LoginAccount
        ),
        name="login",
    ),
    # viewset URLs
    path("api/message/queryset2", viewsets.MessageViewSet.as_view({"get": "list"})),
    path(
        "api/message/queryset2_id/<int:pk>",
        viewsets.MessageViewSet.as_view({"get": "retrieve"}),
    ),
    path(
        "api/message/queryset2_create/",
        viewsets.MessagePostViewSet.as_view({"post": "create"}),
    ),
    path(
        "api/message/queryset2_p_update/<int:pk>",
        viewsets.MessageViewSet.as_view({"patch": "partial_update"}),
    ),
    path(
        "api/message/queryset2_update/<int:pk>",
        viewsets.MessageViewSet.as_view({"patch": "update"}),
    ),
    path(
        "api/message/queryset2_delete/<int:pk>",
        viewsets.MessageViewSet.as_view({"delete": "destroy"}),
    ),
    path("api/user/queryset2", viewsets.UserViewSet.as_view({"get": "list"})),
    path(
        "api/user/queryset2_id/<int:pk>",
        viewsets.UserViewSet.as_view({"get": "retrieve"}),
    ),
    # APIView URLs
    path("api/queryset", viewsets.MessageAPIView.as_view()),
    path("api/queryset_user", viewsets.MessagesPerUserAPIView.as_view()),
]
