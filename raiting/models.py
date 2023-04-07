from django.db import models
from users.models import User


class ContUs(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField(max_length=1500, blank=True, null=True)

    def __str__(self):
        return self.name


class ReviewUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    message = models.TextField(max_length=3000, blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)
