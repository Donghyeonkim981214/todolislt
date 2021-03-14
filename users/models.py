from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

class User(AbstractUser):

    """User model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )

    email = models.EmailField(blank=True, null = True, max_length=254)

    birthday = models.DateField(blank=True, null = True)

    bio = models.TextField(default="Write some details about yourself", blank=True, null=True)

    def get_absolute_url(self):
        return reverse("user:profile", kwargs={"pk": self.pk})