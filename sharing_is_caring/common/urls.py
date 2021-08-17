from django.urls import path

from sharing_is_caring.common.views import LandingPage, AboutUsView, ListPostsView, ListPostsNeededView, \
    ListPostsGiveAwayView

urlpatterns = (
    path('', LandingPage.as_view(), name='index'),
    path('list-posts/', ListPostsView.as_view(), name='list items'),
path('list-posts-needed/', ListPostsNeededView.as_view(), name='list needed items'),
    path('list-posts-give-away/', ListPostsGiveAwayView.as_view(), name='list give-away items'),

    path('about-us/', AboutUsView.as_view(), name='about us')
)
