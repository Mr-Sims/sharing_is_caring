from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

UserModel = get_user_model()


letters_validator = RegexValidator(r'^[a-zA-Z ]*$', 'Only letters allowed')


class Post(models.Model):
    ITEM_CHOICE_TOY = 'Toy'
    ITEM_CHOICE_CLOTHES = 'Clothes'
    ITEM_CHOICE_TOOL = 'Tool'

    ITEM_CHOICES = (
        (ITEM_CHOICE_TOY, 'Toy'),
        (ITEM_CHOICE_CLOTHES, 'Clothes'),
        (ITEM_CHOICE_TOOL, 'Tool'),
    )

    CONDITION_CHOICE_NEW = 'Brand new'
    CONDITION_CHOICE_USED = 'Used'
    CONDITION_CHOICE_USED_W_PROBLEMS = 'Used with some issues'

    CONDITION_CHOICES = (
        (CONDITION_CHOICE_NEW, 'Brand new'),
        (CONDITION_CHOICE_USED, 'Used'),
        (CONDITION_CHOICE_USED_W_PROBLEMS, 'Used with some issues'),
    )

    POST_CHOICE_SEARCHING = 'Search'
    POST_CHOICE_GIVEAWAY = 'Give-away'

    POST_CHOICES = (
        (POST_CHOICE_SEARCHING, 'Search'),
        (POST_CHOICE_GIVEAWAY, 'Give-away'),
    )

    name = models.CharField(
        max_length=30,
        validators=[letters_validator],
    )
    description = models.TextField()

    item_type = models.CharField(
        max_length=7,
        choices=ITEM_CHOICES,
    )
    condition = models.CharField(
        max_length=21,
        choices=CONDITION_CHOICES,
    )
    type = models.CharField(
        max_length=9,
        choices=POST_CHOICES,
    )
    image = models.ImageField(
        upload_to='items',
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
