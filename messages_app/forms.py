from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Message


class CreateAccount(UserCreationForm):
    """
    User creation form
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


class LoginAccount(AuthenticationForm):
    """
    User log in form
    """

    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "ej: pepito69", "class": "campos"})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "campos"}))


class CreateMessage(forms.ModelForm):
    """
    Message creation form
    """

    class Meta:
        model = Message
        fields = ("title", "content")

    # añadimos required=false puesto que queremos que se pueda dejar el titulo en blanco
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "ej: pepito69", "class": "campos"}
        ),
        required=False,
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "ej: pepito69",
                "class": "campos",
                "rows": 5,
                "cols": 20,
            }
        )
    )
