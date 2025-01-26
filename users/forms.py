from email.mime import image
from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)

from users.models import User

# класс формы авторизации
class UserLoginForm(AuthenticationForm): # AuthenticationForm - класс формы авторизации по умолчанию Django
    pass

    

# класс формы регистрации
class UserRegistrationForm(UserCreationForm):# UserCreationForm - класс формы регистрации по умолчанию Django

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

   


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "image",
        )

   