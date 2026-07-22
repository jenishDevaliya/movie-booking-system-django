from django.shortcuts import render, get_object_or_404
from .models import Movie


def home(request):
    movies = Movie.objects.all().order_by("-created_at")
    return render(request, "home.html", {
        "movies": movies
    })


def movie_list(request):
    movies = Movie.objects.all().order_by("-created_at")
    return render(request, "movies/movie_list.html", {
        "movies": movies
    })


def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, "movie_detail.html", {
        "movie": movie
    })