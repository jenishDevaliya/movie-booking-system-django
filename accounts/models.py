from django.db import models
from django.contrib.auth.models import AbstractUser
from theaters.models import Country, State, City


class User(AbstractUser):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    STATUS_CHOICES = (
        (0, "Active"),
        (1, "Inactive"),
    )

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)

    phone = models.CharField(max_length=15, unique=True)
    profile_image = models.ImageField(upload_to="user_dp/", blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return self.username