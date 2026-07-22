from django.contrib import admin
from .models import Seat, Show, Booking, Payment


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "screen",
        "seat_number",
    )

    search_fields = (
        "seat_number",
        "screen__screen_name",
    )

    list_filter = (
        "screen",
    )

    ordering = ("id",)


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "movie",
        "screen",
        "show_date",
        "show_time",
        "ticket_price",
        "is_active",
    )

    search_fields = (
        "movie__title",
        "screen__screen_name",
        "screen__theater__theater_name",
    )

    list_filter = (
        "show_date",
        "screen",
        "is_active",
    )

    ordering = (
        "show_date",
        "show_time",
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "show",
        "total_amount",
        "status",
        "booking_date",
    )

    search_fields = (
        "user__username",
        "show__movie__title",
    )

    list_filter = (
        "status",
        "booking_date",
    )

    filter_horizontal = (
        "seats",
    )

    ordering = (
        "-booking_date",
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "booking",
        "payment_method",
        "transaction_id",
        "payment_status",
        "payment_date",
    )

    search_fields = (
        "transaction_id",
        "booking__user__username",
    )

    list_filter = (
        "payment_method",
        "payment_status",
    )

    ordering = (
        "-payment_date",
    )