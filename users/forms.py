# forms.py создаётся приложении, если нужно создать свои собственные формы — он не обязателен и не создаётся автоматически Django.
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User

# AuthenticationForm - проверяет логин и пароль пользователя,выполняет аутентификацию через систему Django,
# UserCreationForm — это встроенная Django-форма, которая используется для регистрации нового пользователя


# ------------------------------Создаем кастомную свою форму для входа в личный кабинет-------------------------------------
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


# ----------------------------------Форма для регистрации нового пользовотеля---------------------------------------
class UserRegistrationForm(UserCreationForm):
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

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите ваше имя",
    #         }
    #     )
    # )
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите вашу фамилию",
    #         }
    #     )
    # )
    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите ваше имя пользователя",
    #         }
    #     )
    # )
    # email = forms.CharField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите ваш email *youremail@example.com",
    #         }
    #     )
    # )
    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите ваш пароль",
    #         }
    #     )
    # )
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Поддтвердите ваш пароль",
    #         }
    #     )
    # )
