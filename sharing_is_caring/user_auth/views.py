from django.contrib.auth import get_user_model, logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.mixins import BootstrapFormViewMixin
from sharing_is_caring.user_auth.forms import SignUpForm, LoginFormTrue

UserModel = get_user_model()


class SignUpView(BootstrapFormViewMixin, CreateView):
    model = UserModel
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInView(BootstrapFormViewMixin, LoginView):
    form_class = LoginFormTrue
    success_url = reverse_lazy('index')
    template_name = 'auth/sign-in.html'


def sign_out_user(request):
    logout(request)
    return redirect('index')
