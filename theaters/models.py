from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["country_name"]
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.country_name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    d_pic = models.ImageField(upload_to="state_images/")
    state_name = models.CharField(max_length=100)

    class Meta:
        ordering = ["state_name"]
        unique_together = ("country", "state_name")

    def __str__(self):
        return self.state_name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)

    class Meta:
        ordering = ["city_name"]
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.city_name
    


class Theater(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="theaters"
    )

    theater_name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    total_screens = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["theater_name"]

    def __str__(self):
        return self.theater_name


class Screen(models.Model):

    SCREEN_TYPES = (
        ("2D", "2D"),
        ("3D", "3D"),
        ("IMAX", "IMAX"),
        ("4DX", "4DX"),
    )

    theater = models.ForeignKey(
        Theater,
        on_delete=models.CASCADE,
        related_name="screens"
    )

    screen_name = models.CharField(max_length=50)

    screen_type = models.CharField(
        max_length=20,
        choices=SCREEN_TYPES,
        default="2D"
    )

    total_rows = models.PositiveIntegerField(default=10)
    seats_per_row = models.PositiveIntegerField(default=12)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.theater.theater_name} - {self.screen_name}"
