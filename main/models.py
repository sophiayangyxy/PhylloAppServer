from datetime import datetime
from django.db import models

# Create your models here.


TYPE_CHOICES = (
    ('tip', 'TIP'),
    ('url', 'LINK'),
    ('longform', 'LONGFORM'),
)


class Poster(models.Model):
    username = models.CharField(max_length=255)
    points = models.IntegerField()

    def __unicode__(self):
        return self.username


class Location(models.Model):
    longitude = models.DecimalField(max_digits=20, decimal_places=10)
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    # radius = models.IntegerField() # Doesn't make sense to put it here?


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Story(models.Model):
    type = models.CharField(choices=TYPE_CHOICES, max_length=10, default='tip')
    title = models.TextField(max_length=140)
    content = models.TextField(max_length=10000)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    originalPoster = models.ForeignKey(Poster, null=True)
    location = models.ForeignKey(Location, null=True)
    tags = models.ManyToManyField(Tag, related_name='related_story')

    @classmethod
    def create(cls, type, title, content, longitude, latitude, tagList):
        loc1 = Location(longitude=longitude, latitude=latitude)
        for t in tagList:
            print t
        loc1.save()
        poster = Poster(username="user4", points=100)
        poster.save()
        tag = Tag(name="story")
        tag.save()
        story = Story(type=type, title=title, content=content)
        story.save()


