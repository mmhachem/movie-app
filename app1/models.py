from django.db import models

class Movie(models.Model):
    GENRE_CHOICES = [
        ('Comedy', 'Comedy'),
        ('Romance', 'Romance'),
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('SciFi', 'Sci-Fi'),
    ]
    MovieTitle   = models.CharField(max_length=200)
    Actor1Name   = models.CharField(max_length=100)
    Actor2Name   = models.CharField(max_length=100, blank=True)
    DirectorName = models.CharField(max_length=100)
    MovieGenre   = models.CharField(max_length=20, choices=GENRE_CHOICES)
    ReleaseYear  = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"
