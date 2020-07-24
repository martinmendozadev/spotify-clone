"""Users model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from spotify.utils.base_model import BaseModel


class User(BaseModel, AbstractUser):
    """User model.

    Extend from Django's Abstract User.
    """

    email = models.EmailField('email address', unique=True)
    is_membership = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user.'
        )
    )
    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address.'
    )
    birthdate = models.DateField(
        'Birthdate',
        blank=True,
        null=True,
    )

    def __str__(self):
        """Return username."""
        return self.username
