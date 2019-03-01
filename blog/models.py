from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="subtitle")
    text = models.TextField(default='Subtitle')
    picture = models.ImageField(default='blog/static/media/default.jpg')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Profile(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture = models.ImageField(default='blog/static/media/default.jpg')
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=20, default="Boxer")
    age = models.IntegerField(default=16)
    fights = models.IntegerField(default=1)
    hometown = models.CharField(max_length=90, default="Alloa")
    first_title = models.CharField(max_length=100, default="", blank=True)
    second_title = models.CharField(max_length=100, default="", blank=True)
    third_title = models.CharField(max_length=100, default="", blank=True)
    fourth_title = models.CharField(max_length=100, default="", blank=True)
    sixth_title = models.CharField(max_length=100, default="", blank=True)
    seventh_title = models.CharField(max_length=100, default="", blank=True)
    eighth_title = models.CharField(max_length=100, default="", blank=True)
    ninth_title = models.CharField(max_length=100, default="", blank=True)
    tenth_title = models.CharField(max_length=100, default="", blank=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.forename + " " + self.surname
