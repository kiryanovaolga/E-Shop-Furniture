from django.contrib.auth.decorators import login_required
from profile import Profile
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import context
from django.urls import reverse

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request):
    # Пользователь уже отправил форму (POST) или пока просто смотрит страницу (GET)?
    if request.method == "POST":
        # Создаём объект формы и передаём в неё данные, которые пользователь заполнил.
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            # Извлекаем имя и пароль пользователя из данных, которые пришли с формы.
            username = request.POST["username"]
            password = request.POST["password"]

            # Проверка пользователя; есть ли такой в базе данных. Если да, вернется объект user
            user = auth.authenticate(username=username, password=password)
            if user:  # Проверяем, действительно ли пользователь найден
                # выполняет вход пользователя на сайт, сохраняя информацию о нём в сессии.
                auth.login(request, user)
                messages.success(request, f"{username}, you successfully logged in!")
                return HttpResponseRedirect(reverse("main:index"))

    # Если запрос не POST, то отображаем опять пустую форму на этой же странице
    else:
        form = UserLoginForm()

    context = {
        "title": "Home - Authorization",
        "form": form,
    }
    return render(request, "users/login.html", context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(
                request, f"{user.username}, you successfully registrated and logged in!"
            )
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    context = {"title": "Home - Registration", "form": form}
    return render(request, "users/registration.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
        )  # при загрузке файла, браузер отправляет его не в POST, а в отдельную структуру FILES.
        if form.is_valid():
            form.save()
            messages.success(request, f"Your profile has been successfully updated!")
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = ProfileForm(
            instance=request.user
        )  # Создаем форму профиля, заполняя её текущими данными авторизованного пользователя.
    context = {
        "title": "Home - Profile",
        "form": form,
    }
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    messages.success(
        request, f"{request.user.username}, you have successfully logged out."
    )
    auth.logout(request)
    return redirect(reverse("main:index"))
