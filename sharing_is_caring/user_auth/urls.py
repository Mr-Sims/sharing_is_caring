from django.urls import path

from sharing_is_caring.user_auth.views import SignUpView, SignInView, sign_out_user

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', sign_out_user, name='sign out'),
)
