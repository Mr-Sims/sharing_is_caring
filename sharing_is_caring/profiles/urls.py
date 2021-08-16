from django.urls import path

from sharing_is_caring.profiles.views import UserProfileDetailsView, EditProfileView

urlpatterns = (
    path('user-profile/<int:pk>', UserProfileDetailsView.as_view(), name='profile details'),
    path('edit-profile/<int:pk>', EditProfileView.as_view(), name='edit profile'),

)
