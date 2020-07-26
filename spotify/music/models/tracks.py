"""Tracks model."""

# Django
from django.db import models

# Utils
from spotify.utils.base_model import BaseModel


class TrackModel(BaseModel):
    """Tracks Model."""
    artist = models.CharField(
        'Artist song',
        max_length=150,
    )
    title = models.CharField(
        'Song title',
        max_length=100,
    )
    album = models.CharField(
        'Album name',
        max_length=100,
    )
    duration = models.CharField(
        'Duration time song',
        max_length=100
    )

    def __str__(self):
        """Return track name."""
        return self.title
