from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='images/default.png')
    bio = models.TextField(max_length=500, default="My Bio")
    name = models.CharField(blank=True, max_length=120)

    def __str__(self):
        return f'{self.user.username} Profile'



