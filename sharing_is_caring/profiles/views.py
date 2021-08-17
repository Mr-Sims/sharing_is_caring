from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView

from core.mixins import BootstrapFormViewMixin
from sharing_is_caring.main_content.models import Post
from sharing_is_caring.profiles.forms import UserProfileForm
from sharing_is_caring.profiles.models import UserProfile

UserModel = get_user_model()


class UserProfileDetailsView(ListView):
    model = UserProfile
    template_name = 'profile/profile_details.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user_id=self.request.user.id)
        context['profile'] = UserProfile.objects.get(user_id=self.request.user.id)
        return context


class EditProfileView(BootstrapFormViewMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profile/edit_profile.html'
    success_url = reverse_lazy('index')


def profile_details(request, pk):
    usermodel = UserModel.objects.get(pk=pk)
    posts = Post.objects.filter(user_id=usermodel.id)
    profile = UserProfile.objects.get(user_id=usermodel.id)
    context = {
        'usermodel': usermodel,
        'posts': posts,
        'profile': profile,
    }
    return render(request, 'profile/foreign_profile_details.html', context)

