from django.conf import settings
from django.db import models


# Create your models here.
class UserTime(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()


class UserActivity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.title
