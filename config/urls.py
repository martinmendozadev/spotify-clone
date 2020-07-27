"""Main URLs module."""

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    # Local
    path('', include(('spotify.users.urls', 'users'), namespace='users')),
    path('music/', include(('spotify.music.urls', 'music'), namespace='music')),
    path('playLists/', include(('spotify.playLists.urls', 'playList'), namespace='playLists')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
