from django.db import models
from artworks.models import Artwork  

class Review(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()

    def __str__(self):
        return f"Review for {self.artwork.name}"
