from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView

from core.mixins import BootstrapFormViewMixin, BootstrapFormMixin
from sharing_is_caring.profiles.forms import UserProfileForm
from sharing_is_caring.profiles.models import UserProfile


class UserProfileDetailsView(DetailView):
    model = UserProfile
    template_name = 'profile/profile_details.html'
    context_object_name = 'profile'

    # object = None
    #
    # def get(self, request, *args, **kwargs):
    #     self.object = UserProfile.objects.get(pk=request.user.id)
    #     return super().get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     self.object = UserProfile.objects.get(pk=request.user.id)
    #     return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['pets'] = Pet.objects.filter(user_id=self.request.user.id)
        context['profile'] = UserProfile.objects.get(user_id=self.request.user.id)
        return context


    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     pet = context['pet']
    #
    #     pet.likes_count = pet.like_set.count()
    #     is_owner = pet.user == self.request.user
    #
    #     is_liked_by_user = pet.like_set.filter(user_id=self.request.user.id).exists()
    #
    #     context['comment_form'] = CommentForm(
    #             initial={
    #                 'pet_pk': self.object.id,
    #             }
    #         )
    #     context['comments'] = pet.comment_set.all()
    #     context['is_owner'] = is_owner
    #     context['is_liked'] = is_liked_by_user
    #
    #     return context


class EditProfileView(BootstrapFormViewMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profile/edit_profile.html'
    success_url = reverse_lazy('index')
