from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from movies.models import Movie
from theaters.models import Theater
from booking.models import Show, Seat, Booking


@login_required(login_url="login")
def theater_selection(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)

    theaters = Theater.objects.filter(
        is_active=True
    ).select_related(
        "city",
        "city__state",
        "city__state__country"
    )

    context = {
        "movie": movie,
        "theaters": theaters,
    }

    return render(
        request,
        "booking/theater_selection.html",
        context,
    )


@login_required(login_url="login")
def show_selection(request, movie_id, theater_id):

    movie = get_object_or_404(
        Movie,
        id=movie_id
    )

    theater = get_object_or_404(
        Theater,
        id=theater_id
    )

    shows = Show.objects.filter(
        movie=movie,
        screen__theater=theater,
        is_active=True
    ).select_related("screen")

    context = {
        "movie": movie,
        "theater": theater,
        "shows": shows,
    }

    return render(
        request,
        "booking/show_selection.html",
        context,
    )


@login_required(login_url="login")
def seat_selection(request, show_id):

    show = get_object_or_404(
        Show,
        id=show_id
    )

    seats = Seat.objects.filter(
        screen=show.screen
    ).order_by("seat_number")

    if request.method == "POST":

        selected_seats = request.POST.getlist("seats")

        if not selected_seats:

            return render(
                request,
                "booking/seat_selection.html",
                {
                    "show": show,
                    "seats": seats,
                    "error": "Please select at least one seat."
                }
            )

        request.session["show_id"] = show.id
        request.session["selected_seats"] = selected_seats

        return redirect("booking_summary")

    context = {
        "show": show,
        "seats": seats,
    }

    return render(
        request,
        "booking/seat_selection.html",
        context,
    )


@login_required(login_url="login")
def booking_summary(request):

    show = get_object_or_404(
        Show,
        id=request.session.get("show_id")
    )

    seat_ids = request.session.get(
        "selected_seats",
        []
    )

    seats = Seat.objects.filter(
        id__in=seat_ids
    )

    total_amount = Decimal(show.ticket_price) * seats.count()

    context = {
        "show": show,
        "seats": seats,
        "total_amount": total_amount,
        "total_seats": seats.count(),
    }

    return render(
        request,
        "booking/booking_summary.html",
        context,
    )