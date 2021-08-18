from django import forms
from django.contrib.auth import get_user_model

from sharing_is_caring.common.models import Comment
from sharing_is_caring.profiles.models import UserProfile


UserModel = get_user_model()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'is_complete',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
