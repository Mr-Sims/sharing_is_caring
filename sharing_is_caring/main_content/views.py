from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from core.mixins import BootstrapFormViewMixin
from sharing_is_caring.main_content.forms import PostUpdateForm
from sharing_is_caring.main_content.models import Post
from sharing_is_caring.profiles.models import UserProfile


class PostDetailsView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'main_content/post_details.html'
    context_object_name = 'post'
    login_url = reverse_lazy('sign in')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context['post']

        profile = UserProfile.objects.get(user_id=self.request.user.id)
        context['profile'] = profile

        is_owner = post.user == self.request.user
        context['is_owner'] = is_owner
        return context


class CreatePostView(LoginRequiredMixin, BootstrapFormViewMixin, CreateView):
    template_name = 'main_content/add_post.html'
    model = Post
    fields = ('name', 'description', 'item_type', 'condition', 'type', 'image')
    success_url = reverse_lazy('list items')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, BootstrapFormViewMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'main_content/update_post.html'
    success_url = reverse_lazy('list items')


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'main_content/delete_post.html'
    success_url = reverse_lazy('list items')