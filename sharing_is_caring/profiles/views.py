from django.shortcuts import render
from django.views.generic import DetailView

from sharing_is_caring.profiles.models import UserProfile


class UserProfileDetailsView(DetailView):
    model = UserProfile
    template_name = 'profile/profile_details.html'
    context_object_name = 'profile'

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