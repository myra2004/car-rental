from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# from common.models import BaseModel


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    # comments = models.ForeignKey('users.Comment', null=True, blank=True)
    comments = models.TextField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return self.username


# class Comment(models.Model):
#     text = models.TextField(max_length=1000, null=True, blank=True)
#
#     def __str__(self):
#         return self.text