from django.db import models
from django.contrib.auth.models import AbstractUser

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    birthday = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    #followed_by = models.ManyToManyField(to=User, blank=True, related_name="favorite_users")


