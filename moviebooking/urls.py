from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # Admin
    path("admin/", admin.site.urls),

    # Home + Movies
    path("", include("movies.urls")),

    # User Authentication
    path("accounts/", include("accounts.urls")),

    # Theater Module
    path("theaters/", include("theaters.urls")),

    # Booking Module
    path("booking/", include("booking.urls")),
]


# Media files (Images, Posters, Profile Photos)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )