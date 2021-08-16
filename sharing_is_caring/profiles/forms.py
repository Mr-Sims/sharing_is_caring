from django import forms

from core.mixins import BootstrapFormViewMixin, BootstrapFormMixin
from sharing_is_caring.profiles.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'is_complete',)

