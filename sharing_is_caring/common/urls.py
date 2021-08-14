from django.urls import path

from sharing_is_caring.common.views import LandingPage, AboutUsView

urlpatterns = (
    path('', LandingPage.as_view(), name='index'),
    path('about-us/', AboutUsView.as_view(), name='about us')
)