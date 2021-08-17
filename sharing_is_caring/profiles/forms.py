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

#
#
# class CommentForm(forms.ModelForm):
#     user_to_be_commented = forms.IntegerField(
#         widget=forms.HiddenInput()
#     )
#
#     class Meta:
#         model = Comment
#         fields = ('comment', 'user_to_be_commented')
#
#     def save(self, commit=True):
#         user_pk = self.cleaned_data['user_pk']
#         user_to_be_commented = UserModel.objects.get(pk=user_pk)
#         comment = Comment(
#             comment=self.cleaned_data['comment'],
#             user_to_be_commented=user_to_be_commented,
#         )
#
#         if commit:
#             comment.save()
#         return comment
