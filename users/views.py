from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import context
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm


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
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    context = {"title": "Home - Registration", "form": form}
    return render(request, "users/registration.html", context)


def profile(request):
    context = {
        "title": "Home - Profile",
    }
    return render(request, "users/profile.html", context)


def logout(request):
    auth.logout(request)
    return redirect(reverse("main:index"))
