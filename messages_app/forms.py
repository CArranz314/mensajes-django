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
        widget=forms.TextInput(attrs={"placeholder": "ej: pepito69", "class": ""}),
        required=False,
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "ej: pepito69",
                "class": "",
                "rows": 5,
                "cols": 35,
            }
        )
    )


# queda feo poner los imports aqui pero es por claridad
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ExampleForm(forms.Form):
    """
    Example from crispyforms documentation
    """

    like_website = forms.TypedChoiceField(
        label="Do you like this website?",
        choices=((1, "Yes"), (0, "No")),
        coerce=lambda x: bool(int(x)),
        widget=forms.RadioSelect,
        initial="1",
        required=True,
    )

    favorite_food = forms.CharField(
        label="What is your favorite food?",
        max_length=80,
        required=True,
    )

    favorite_color = forms.CharField(
        label="What is your favorite color?",
        max_length=80,
        required=True,
    )

    favorite_number = forms.IntegerField(
        label="Favorite number",
        required=False,
    )

    notes = forms.CharField(
        label="Additional notes or feedback",
        required=False,
    )

    # usamos helper para personalizar el formulario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # creamos una instancia de FormHelper
        self.helper = FormHelper()
        self.helper.form_id = "id-exampleForm"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_survey"

        self.helper.add_input(Submit("submit", "Submit"))
