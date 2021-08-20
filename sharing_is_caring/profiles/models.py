from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

UserModel = get_user_model()
letters_validator = RegexValidator(r'^[a-zA-Z]*$', 'Only letters allowed')

class UserProfile(models.Model):
    TYPE_CHOICE_MALE = 'male'
    TYPE_CHOICE_FEMALE = 'female'

    TYPE_CHOICES = (
        (TYPE_CHOICE_MALE, 'Male'),
        (TYPE_CHOICE_FEMALE, 'Female'),
    )
    first_name = models.CharField(
        max_length=20,
        blank=True,
        validators=[letters_validator],
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
        validators=[letters_validator],
    )
    address = models.CharField(
        max_length=30,
        blank=True,
    )
    city = models.CharField(
        max_length=30,
        blank=True,
        validators=[letters_validator],
    )
    number_of_children = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    gender = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
        blank=True,
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    is_complete = models.BooleanField(
        default=False,
    )


from .signals import *
