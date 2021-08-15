from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from sharing_is_caring.profiles.models import UserProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile(
            user=instance,
        )
        profile.save()


@receiver(pre_save, sender=UserProfile)
def check_profile_complete(sender, instance: UserProfile, **kwargs):
    if instance.address and \
            instance.first_name and \
            instance.last_name and \
            instance.city and\
            instance.gender and instance.number_of_children:

        instance.is_complete = True
        return
