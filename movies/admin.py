from django.contrib import admin
from .models import Genre, Director, Actor, Movie, Review, Watchlist


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "genre",
        "director",
        "release_year",
        "language",
        "certificate",
        "duration",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
    )

    list_filter = (
        "genre",
        "language",
        "certificate",
        "release_year",
        "director",
    )

    filter_horizontal = ("actors",)

    ordering = ("-created_at",)

    fieldsets = (
        ("Movie Information", {
            "fields": (
                "title",
                "description",
                "release_year",
                "genre",
                "director",
                "actors",
            )
        }),
        ("Movie Details", {
            "fields": (
                "certificate",
                "movie_type",
                "language",
                "duration",
            )
        }),
        ("Media", {
            "fields": (
                "poster",
                "trailer",
            )
        }),
    )