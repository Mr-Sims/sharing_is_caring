from django.urls import path

from sharing_is_caring.main_content.views import ListPostsView

urlpatterns = (
    path('list-items/', ListPostsView.as_view(), name='list items'),
)
