from django.db import models


# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='artists', blank=True, null=True)
    nb_album = models.IntegerField()
    nb_fan = models.IntegerField()

    def __str__(self):
        return f"{self.id}. {self.name} ({self.nb_album} albums) ({self.nb_fan} fans)"


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='albums', blank=True, null=True)
    release_date = models.DateField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}. {self.title} (release_date: {self.release_date})"


class Track(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    title_short = models.CharField(max_length=50, blank=True, null=True)
    picture = models.ImageField(upload_to='tracks', blank=True, null=True)
    duration = models.IntegerField()
    rank = models.IntegerField()
    release_date = models.DateField()
    bpm = models.IntegerField(null=True, blank=True)
    gain = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.duration} seconds)"
