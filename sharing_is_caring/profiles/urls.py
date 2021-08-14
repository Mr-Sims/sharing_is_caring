from django.urls import path

from sharing_is_caring.profiles.views import UserProfileDetailsView

urlpatterns = (
    path('user-profile/<int:pk>', UserProfileDetailsView.as_view(), name='profile details'),

)
