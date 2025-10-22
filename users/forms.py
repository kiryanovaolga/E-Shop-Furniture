# forms.py создаётся приложении, если нужно создать свои собственные формы — он не обязателен и не создаётся автоматически Django.
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User

# AuthenticationForm - проверяет логин и пароль пользователя,выполняет аутентификацию через систему Django,


# Создаем кастомную свою форму
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User  # С какой моделью будет работать форма
        fields = [  # какие поля отображать в форме при входе. Должны совпадать полями, какие в модели User
            "username",
            "password",
        ]

    username = forms.CharField()
    password = forms.CharField()

    # username = forms.CharField(
    #     label="Username",
    #     widget=forms.TextInput(
    #         attrs={
    #             "autofocus": True,
    #             "class": "form-control",
    #             "placeholder": "User Name",
    #         }
    #     ),
    # )
    # password = forms.CharField(
    #     label="Password",
    #     widget=forms.PasswordInput(  # это то, как Django показывает поле формы в HTML.
    #         attrs={
    #             "autocomplete": "current-password",
    #             "class": "form-control",
    #             "placeholder": "User Password",
    #         }
    #     ),
    # )
