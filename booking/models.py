from django.db import models
from django.conf import settings
from movies.models import Movie
from theaters.models import Screen


class Show(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="shows"
    )

    screen = models.ForeignKey(
        Screen,
        on_delete=models.CASCADE,
        related_name="shows"
    )

    show_date = models.DateField()

    show_time = models.TimeField()

    ticket_price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "show_date",
            "show_time",
        ]

    def __str__(self):
        return f"{self.movie.title} - {self.show_date} {self.show_time}"


class Seat(models.Model):
    screen = models.ForeignKey(
        Screen,
        on_delete=models.CASCADE,
        related_name="seats"
    )

    seat_number = models.CharField(max_length=10)

    class Meta:
        unique_together = (
            "screen",
            "seat_number",
        )

        ordering = [
            "seat_number",
        ]

    def __str__(self):
        return self.seat_number


class Booking(models.Model):

    STATUS = (
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Cancelled", "Cancelled"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    show = models.ForeignKey(
        Show,
        on_delete=models.CASCADE
    )

    seats = models.ManyToManyField(
        Seat
    )

    booking_date = models.DateTimeField(
        auto_now_add=True
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Pending"
    )

    def __str__(self):
        return f"Booking #{self.id}"


class Payment(models.Model):

    METHODS = (
        ("UPI", "UPI"),
        ("Card", "Card"),
        ("Net Banking", "Net Banking"),
        ("Cash", "Cash"),
    )

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE
    )

    payment_method = models.CharField(
        max_length=20,
        choices=METHODS
    )

    transaction_id = models.CharField(
        max_length=100,
        unique=True
    )

    payment_status = models.BooleanField(
        default=False
    )

    payment_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.transaction_id