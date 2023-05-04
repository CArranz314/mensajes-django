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
    path("api/queryset", viewsets.MessageAPIViewSet.as_view()),
    path("api/queryset_user", viewsets.MessagesPerUserAPIViewSet.as_view()),
]
