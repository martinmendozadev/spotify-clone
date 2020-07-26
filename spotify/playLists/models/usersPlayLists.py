"""Users Play Lists Relationships."""

# Django
from django.db import models

# Utils
from spotify.utils.base_model import BaseModel


class PlayLists(BaseModel):
    """Users Play List Storage."""
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
    )
    track = models.ForeignKey(
        'music.TrackModel',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """Return name PlayList"""
        return f'{self.user} -> {self.track}'
