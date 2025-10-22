from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser


# AbstractUser = готовая модель User, но расширяемая. Eсли нужно дополнить стандартного пользователя.
class User(AbstractUser):
    image = models.ImageField(
        upload_to="users_images", blank=True, null=True, verbose_name="avatar"
    )

    class Meta:
        db_table = "user"  # название нашей таблицы БД
        verbose_name = "User"  # название нашей таблицы в админ панеле в ед. ч.(Select Category to change...)
        verbose_name_plural = "Users"  # название нашей таблицы в админ панеле во мн. ч.

    def __str__(self):
        return self.username
