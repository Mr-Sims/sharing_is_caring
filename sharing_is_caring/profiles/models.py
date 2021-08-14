from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class UserProfile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True,
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
    )
    address = models.CharField(
        max_length=30,
        blank=True,
    )
    city = models.CharField(
        max_length=30,
        blank=True,
    )
    number_of_children = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from .signals import *
