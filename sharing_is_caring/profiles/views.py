from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, ListView

from core.mixins import BootstrapFormViewMixin
from sharing_is_caring.common.models import Comment
from sharing_is_caring.main_content.models import Post
from sharing_is_caring.profiles.forms import UserProfileForm, CommentForm
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
        context['comments'] = Comment.objects.filter(user_to_be_commented=self.request.user.id)
        return context


class EditProfileView(BootstrapFormViewMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profile/edit_profile.html'
    success_url = reverse_lazy('index')


@login_required()
def profile_details(request, pk):
    usermodel = UserModel.objects.get(pk=pk)
    posts = Post.objects.filter(user_id=usermodel.id)
    profile = UserProfile.objects.get(user_id=usermodel.id)
    comments = Comment.objects.filter(user_to_be_commented=usermodel.id)
    context = {
        'comments': comments,
        'usermodel': usermodel,
        'posts': posts,
        'profile': profile,
        'comment_form': CommentForm(
            initial={
                'user_to_be_liked': pk,
            }
        ),
    }
    return render(request, 'profile/foreign_profile_details.html', context)


class PostOnlyView(View):
    form_class = None

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        pass

    def form_invalid(self, form):
        pass


class CommentProfileView(LoginRequiredMixin, PostOnlyView):
    form_class = CommentForm

    def form_valid(self, form):
        user_to_be_commented = UserProfile.objects.get(pk=self.kwargs['pk'])
        comment = Comment(
            comment=form.cleaned_data['comment'],
            user_to_be_commented=user_to_be_commented,
            user=self.request.user,
        )
        comment.save()
        return redirect('foreign profile details', user_to_be_commented.pk)

    def form_invalid(self, form):
        pass
