from django.db import models
from musician.models import Musician

# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_release_dt = models.DateField()
    rating_choices = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    album_rating = models.CharField(
        max_length=1,
        choices=rating_choices,
        default='1')

    def __str__(self):
        return f"Album:- {self.name}"
