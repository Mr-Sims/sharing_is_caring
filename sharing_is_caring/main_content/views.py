from django.shortcuts import render
from django.views.generic import ListView

from sharing_is_caring.main_content.models import Post


class ListPostsView(ListView):
    model = Post
    template_name = 'main_content/list_items.html'
    context_object_name = 'posts'
    paginate_by = 8
