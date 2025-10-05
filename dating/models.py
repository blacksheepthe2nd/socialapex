from django.db import models
from django.contrib.auth.models import User

class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    interests = models.ManyToManyField(Interest, blank=True)

    def __str__(self):
        return self.user.username

# Temporarily comment out ProfilePhoto to avoid Pillow dependency
# class ProfilePhoto(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='photos')
#     image = models.ImageField(upload_to='profile_photos/')
#     is_primary = models.BooleanField(default=False)
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Photo for {self.profile.user.username}"
