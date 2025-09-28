from django.apps import AppConfig

"""
app / settings / urls — «организация проекта», какой проект и какие приложения подключены
"""


class GoodsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "goods"
    verbose_name = "Goods Range"
