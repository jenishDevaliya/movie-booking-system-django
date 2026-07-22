from django.db import models
from django.conf import settings
from movies.models import Movie
from theaters.models import Screen


class Seat(models.Model):
    screen = models.ForeignKey(
        Screen,
        on_delete=models.CASCADE,
        related_name="seats"
    )

    seat_number = models.CharField(max_length=10)

    class Meta:
        unique_together = ("screen", "seat_number")
        ordering = ["seat_number"]

    def __str__(self):
        return f"{self.screen.screen_name} - {self.seat_number}"


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
        ordering = ["show_date", "show_time"]

    def __str__(self):
        return (
            f"{self.movie.title} - "
            f"{self.show_date} "
            f"{self.show_time}"
        )


class Booking(models.Model):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Cancelled", "Cancelled"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    show = models.ForeignKey(
        Show,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    seats = models.ManyToManyField(
        Seat,
        related_name="bookings"
    )

    booking_date = models.DateTimeField(auto_now_add=True)

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    class Meta:
        ordering = ["-booking_date"]

    def __str__(self):
        return f"Booking #{self.id} - {self.user.username}"


class Payment(models.Model):
    PAYMENT_METHODS = (
        ("Cash", "Cash"),
        ("UPI", "UPI"),
        ("Card", "Card"),
        ("Net Banking", "Net Banking"),
    )

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE,
        related_name="payment"
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS
    )

    transaction_id = models.CharField(
        max_length=100,
        unique=True
    )

    payment_date = models.DateTimeField(auto_now_add=True)

    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.transaction_id