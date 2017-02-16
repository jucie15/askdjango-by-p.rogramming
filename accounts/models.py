from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length = 32)
    address = models.CharField(max_length = 128)

    def __str__(self):
        return self.user
