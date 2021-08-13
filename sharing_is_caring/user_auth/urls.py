from django.urls import path

from sharing_is_caring.user_auth.views import LandingPage, landing_page

urlpatterns = (
    path('', LandingPage.as_view(), name='index'),
)