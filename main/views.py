from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(request):
    categories = Categories.objects.all()
    context = {
        "title": "Home - main page",
        "content": "Furniture Shop Home",
        "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - About us",
        "content": "About us",
        "text_on_page": "Modern, stylish furniters for your comfortable life",
    }
    return render(request, "main/about.html", context)
