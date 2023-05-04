from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Mensaje


class CrearCuenta(UserCreationForm):
    """
    Formulario de creación de usuarios
    """

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    # para personalizar los input del formulario se hace desde aqui
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "ej: pepito69", "class": "campos"})
    )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "campos"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "campos"}))


class AccederCuenta(AuthenticationForm):
    """
    Formulario de registro de usuarios
    """

    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "ej: pepito69", "class": "campos"})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "campos"}))


class CrearMensaje(forms.ModelForm):
    """
    Formulario para crear mensajes
    """

    class Meta:
        model = Mensaje
        fields = ("titulo", "contenido")

    # añadimos required=false puesto que queremos que se pueda dejar el titulo en blanco
    titulo = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "ej: pepito69", "class": "campos"}
        ),
        required=False,
    )
    contenido = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "ej: pepito69",
                "class": "campos",
                "rows": 5,
                "cols": 20,
            }
        )
    )
