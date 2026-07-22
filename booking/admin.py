from django.contrib import admin
from .models import Show, Seat, Booking, Payment


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = (
        "movie",
        "screen",
        "show_date",
        "show_time",
        "ticket_price",
        "is_active",
    )


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = (
        "screen",
        "seat_number",
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "show",
        "total_amount",
        "status",
        "booking_date",
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "booking",
        "payment_method",
        "transaction_id",
        "payment_status",
    )