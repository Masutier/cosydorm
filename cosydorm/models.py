from django.db import models


class ContUs(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField(max_length=1500, blank=True, null=True)

    def __str__(self):
        return self.name
