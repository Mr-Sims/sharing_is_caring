from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.mixins import BootstrapFormViewMixin
from sharing_is_caring.user_auth.forms import SignUpForm, LoginForm

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
    form_class = LoginForm
    success_url = reverse_lazy('index')
    template_name = 'auth/sign-in.html'



class SignOutView(LogoutView):
    next_page = reverse_lazy('index')
