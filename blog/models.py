from django.conf import settings
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="subtitle")
    text = models.TextField(default="")
    # picture = models.ImageField(default='blog/static/media/default.jpg')
    picture = CloudinaryField('image')
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
    picture = CloudinaryField('image')
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=20, default="Boxer", blank=True)
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


class Event(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    eventTitle = models.CharField(max_length=100, default="", blank=True)
    eventDate = models.CharField(max_length=100, default="", blank=True)
    location = models.CharField(max_length=100, default="", blank=True)
    price = models.CharField(max_length=100, default="", blank=True)
    homeFighter = models.CharField(max_length=100, default="", blank=True)
    homeClub = models.CharField(max_length=100, default="", blank=True)
    awayFighter = models.CharField(max_length=100, default="", blank=True)
    awayClub = models.CharField(max_length=100, default="", blank=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.eventTitle


class GalleryPhoto(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture = CloudinaryField('image')
    caption = models.CharField(max_length=100, default="", blank=True)
    credit = models.CharField(max_length=100, default="", blank=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.caption


# class Coach(models.Model):
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     picture = CloudinaryField('image')
#     forename = models.CharField(max_length=100, default="", blank=True)
#     surname = models.CharField(max_length=100, default="", blank=True)
#     role = models.CharField(max_length=100, default="Coach", blank=True)
#     age = models.IntegerField(default=None)
#     experience = models.IntegerField(default=None)
#     # bio = models.TextField(default="")
#     published_date = models.DateTimeField(blank=True, null=True)


class Staff(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture = CloudinaryField('image')
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=20, default="Boxer", blank=True)
    age = models.IntegerField(default=16)
    experience = models.IntegerField(default=1)
    bio = models.TextField(default="")
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.forename + " " + self.surname

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.forename + " " + self.surname
