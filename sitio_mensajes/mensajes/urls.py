from django.urls import path

from django.contrib.auth import views as auth_views

from .forms import AccederCuenta
from . import views


app_name = "mensajes"
urlpatterns = [
    path("", views.listar, name="listar"),
    path("<int:pk>", views.ver_mensaje, name="ver_mensaje"),
    path("nuevo/", views.nuevo_mensaje, name="nuevo_mensaje"),
    path("crear_cuenta/", views.crear_cuenta, name="crear_cuenta"),
    # logout y login son de django, no propias
    path(
        "salir/",
        auth_views.LogoutView.as_view(next_page="mensajes:listar"),
        name="salir",
    ),
    path(
        "registro/",
        auth_views.LoginView.as_view(
            template_name="mensajes/registro.html", authentication_form=AccederCuenta
        ),
        name="registro",
    ),
]
