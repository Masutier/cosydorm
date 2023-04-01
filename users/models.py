from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


INSTITUTE = (
    ('Private', 'Private'),
    ('College', 'College'),
    ('University', 'University'),
    ('Airbnb', 'Airbnb'),
    ('Other', 'Other')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=False, blank=False)
    institute = models.CharField(max_length=40, choices=INSTITUTE)
    building = models.CharField(max_length=40, null=True, blank=True)
    room = models.CharField(max_length=40, null=True, blank=True)
    address = models.CharField(max_length=200, null=False, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    zip = models.IntegerField(null=False, blank=False)


    def __str__(self):
        return f'{self.user.username} Profile'
