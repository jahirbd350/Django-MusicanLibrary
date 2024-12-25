from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    instrument_type = models.CharField(max_length=20)

    def __str__(self):
        return f"Musician - {self.first_name} {self.last_name}"
