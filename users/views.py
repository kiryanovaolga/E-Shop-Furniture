from django.shortcuts import render
from django.template import context


def login(request):
    context = {
        "title": "Home - Authorization",
    }
    return render(request, "users/login.html", context)


def registration(request):
    context = {
        "title": "Home - Registration",
    }
    return render(request, "users/registration.html", context)


def profile(request):
    context = {
        "title": "Home - Profile",
    }
    return render(request, "users/profile.html", context)


def logout(request): ...
