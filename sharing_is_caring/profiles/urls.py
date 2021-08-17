from django.urls import path

from sharing_is_caring.profiles.views import UserProfileDetailsView, EditProfileView, profile_details, \
    CommentProfileView

urlpatterns = (
    path('user-profile/<int:pk>', UserProfileDetailsView.as_view(), name='profile details'),
    path('edit-profile/<int:pk>', EditProfileView.as_view(), name='edit profile'),

    path('profile/<int:pk>', profile_details, name='foreign profile details'),
    path('comment/<int:pk>', CommentProfileView.as_view(), name='comment profile')

)
