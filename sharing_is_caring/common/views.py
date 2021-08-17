from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from sharing_is_caring.main_content.models import Post
from sharing_is_caring.profiles.models import UserProfile


class LandingPage(TemplateView):
    template_name = 'common/index.html'

    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['profile'] = UserProfile.objects.get(user_id=self.request.user.id)
        return context


class ListPostsView(ListView):
    model = Post
    template_name = 'common/list_posts.html'
    context_object_name = 'posts'
    paginate_by = 8


class ListPostsNeededView(ListView):
    model = Post
    template_name = 'common/list_posts_needed.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(type="Search")
        return context


class ListPostsGiveAwayView(ListView):
    model = Post
    template_name = 'common/list_posts_give_away.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(type="Give-away")
        return context


class AboutUsView(TemplateView):
    template_name = 'common/about-us.html'

