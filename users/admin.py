from django.contrib import admin
from users.models import User

# Регестрируем model User
admin.site.register(User)
