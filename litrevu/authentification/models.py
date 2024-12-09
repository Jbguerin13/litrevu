from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    REVIEW_CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = (
        (REVIEW_CREATOR, "créateur de review"),
        (SUBSCRIBER, "abonné"),
    )
    role = models.CharField(
        max_length=30, choices=ROLE_CHOICES, verbose_name="rôle", default=REVIEW_CREATOR
    )
    follows = models.ManyToManyField(
        "self",
        limit_choices_to={"role": REVIEW_CREATOR},
        symmetrical=False,
        verbose_name="follow",
    )

    pass
