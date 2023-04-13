from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    INSTITUTE = (
        ('Private', 'Private'),
        ('College', 'College'),
        ('University', 'University'),
        ('Airbnba', 'Airbnba'),
        ('Airbnbh', 'Airbnbh'),
        ('Other', 'Other')
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, null=False, blank=False)
    institute = models.CharField(max_length=80, choices=INSTITUTE)
    address1 = models.CharField(max_length=200, null=True, blank=True)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=80, null=True, blank=True)
    state = models.CharField(max_length=40, null=True, blank=True, default='Florida')
    zip = models.CharField(max_length=5, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.user.username)
