from django.db import models
from django.conf import settings
from theaters.models import Country, State, City


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Director(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    d_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    d_state = models.ForeignKey(State, on_delete=models.CASCADE)
    d_city = models.ForeignKey(City, on_delete=models.CASCADE)

    d_name = models.CharField(max_length=100)
    d_bio = models.TextField()
    d_nationality = models.CharField(max_length=100)
    d_awards = models.TextField(blank=True, null=True)
    d_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.d_name


class Actor(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    a_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    a_state = models.ForeignKey(State, on_delete=models.CASCADE)
    a_city = models.ForeignKey(City, on_delete=models.CASCADE)

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    a_pic = models.ImageField(upload_to="actor_images/")
    a_name = models.CharField(max_length=100)
    a_bio = models.TextField()
    a_nationality = models.CharField(max_length=100)
    a_awards = models.TextField(blank=True, null=True)
    a_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    a_birthdate = models.DateField()

    def __str__(self):
        return self.a_name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.PositiveIntegerField()

    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name="movies"
    )

    actors = models.ManyToManyField(
        Actor,
        related_name="movies"
    )

    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name="movies"
    )

    poster = models.ImageField(upload_to="movie_posters/")
    trailer = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    certificate = models.CharField(max_length=20, blank=True, null=True)

    movie_type = models.CharField(max_length=20, blank=True, null=True)

    language = models.CharField(max_length=50, blank=True, null=True)

    duration = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    rating = models.PositiveSmallIntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"


class Watchlist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="watchlists"
    )

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="watchlists"
    )

    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "movie")

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"