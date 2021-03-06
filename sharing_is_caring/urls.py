from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('sharing_is_caring.common.urls')),
    path('auth/', include('sharing_is_caring.user_auth.urls')),
    path('profiles/', include('sharing_is_caring.profiles.urls')),
    path('main/', include('sharing_is_caring.main_content.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
