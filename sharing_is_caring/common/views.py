from django.shortcuts import render
from django.views.generic import TemplateView

from sharing_is_caring.profiles.models import UserProfile


class LandingPage(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.get(user_id=self.request.user.id)
        return context


class AboutUsView(TemplateView):
    template_name = 'common/about-us.html'
