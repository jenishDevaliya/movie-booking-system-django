from django.contrib import admin
from .models import Country, State, City, Theater, Screen


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "country_name",
    )

    search_fields = (
        "country_name",
    )

    ordering = (
        "country_name",
    )


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "state_name",
        "country",
        "d_pic",
    )

    search_fields = (
        "state_name",
        "country__country_name",
    )

    list_filter = (
        "country",
    )

    ordering = (
        "state_name",
    )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "city_name",
        "state",
    )

    search_fields = (
        "city_name",
        "state__state_name",
        "state__country__country_name",
    )

    list_filter = (
        "state",
    )

    ordering = (
        "city_name",
    )


@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "theater_name",
        "city",
        "phone",
        "total_screens",
        "is_active",
    )

    search_fields = (
        "theater_name",
        "city__city_name",
    )

    list_filter = (
        "city",
        "is_active",
    )


@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "screen_name",
        "theater",
        "screen_type",
        "total_rows",
        "seats_per_row",
        "is_active",
    )

    search_fields = (
        "screen_name",
        "theater__theater_name",
    )

    list_filter = (
        "screen_type",
        "is_active",
    )