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
    is_favorite = models.BooleanField(
        default=False
    )

    def __str__(self):
        """Return user PlayList"""
        return (
            f"'username': {self.user}, "
            f"'is_favorite': {self.is_favorite}, "
            f"'title': {self.track.title}, "
            f"'album': {self.track.album}, "
            f"'duration': {self.track.duration}"
        )
