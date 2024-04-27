from django.db import models


# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


# many to many
class Album(models.Model):
    name = models.CharField(max_length=100)
    release_year = models.IntegerField()
    artists = models.ManyToManyField(Artist)

    def __str__(self):
        return f'Album{self.name}-{self.release_year}'


class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')

    def __str__(self):
        return self.title
