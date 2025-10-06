from django.urls import path
from goods import views

app_name = "goods"

urlpatterns = [
    # Сначала проверяем фиксированные пути (search/, product/...)
    path("search/", views.catalog, name="search"),
    # Только потом уже идёт <slug:category_slug>/
    path("<slug:category_slug>/", views.catalog, name="index"),
    path("product/<slug:product_slug>/", views.product, name="product"),
]
