from django.urls import path

from sharing_is_caring.main_content.views import PostDetailsView, CreatePostView, UpdatePostView, \
    DeletePostView

urlpatterns = (
    path('add-post/', CreatePostView.as_view(), name='add post'),
    path('update-post/<int:pk>', UpdatePostView.as_view(), name='update post'),
    path('post-details/<int:pk>', PostDetailsView.as_view(), name='post details'),
    path('delete-post/<int:pk>', DeletePostView.as_view(), name='delete post')
)
