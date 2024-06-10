from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _

# Create your models here.


class UserRoles(models.TextChoices):
    ADMIN = "admin", _('Администратор')
    AUTHOR = "author", _('Автор')

class User(AbstractUser):
    first_name = models.CharField(verbose_name='Имя', max_length=100)
    last_name = models.CharField(verbose_name='Фамилия', max_length=100)
    display_name = models.CharField(verbose_name='Отображаемое имя', max_length=400, blank=True)

    staff_role = models.CharField(verbose_name='Роль', max_length=100, choices=UserRoles.choices, null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return self.email
