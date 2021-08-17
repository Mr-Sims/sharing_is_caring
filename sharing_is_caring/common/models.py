from django.contrib.auth import get_user_model
from django.db import models

from sharing_is_caring.profiles.models import UserProfile

UserModel = get_user_model()


class Comment(models.Model):
    comment = models.TextField()

    user_to_be_commented = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


