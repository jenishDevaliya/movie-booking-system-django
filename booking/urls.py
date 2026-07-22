from django.urls import path
from . import views

urlpatterns = [
    path(
        "movie/<int:movie_id>/theaters/",
        views.theater_selection,
        name="theater_selection",
    ),
      path(
        "movie/<int:movie_id>/theater/<int:theater_id>/shows/",
        views.show_selection,
        name="show_selection",
    ),
      path(
        "show/<int:show_id>/seats/",
        views.seat_selection,
        name="seat_selection",
    ),
    path(
        "booking-summary/",
        views.booking_summary,
        name="booking_summary",
    ),
]