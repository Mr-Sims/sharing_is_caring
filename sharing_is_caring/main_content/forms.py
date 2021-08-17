from django import forms

from sharing_is_caring.main_content.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)


class PostUpdateForm(PostCreateForm):
    class Meta:
        model = Post
        exclude = ('user',)

        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly'
                }
            )
        }

