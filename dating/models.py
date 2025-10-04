from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Interest(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        app_label = 'dating'
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    about = models.TextField()
    profile_image = models.URLField(max_length=500, blank=True, null=True)  # Add this field
    interests = models.ManyToManyField(Interest, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        app_label = 'dating'
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.pk})

class ProfilePhoto(models.Model):
    profile = models.ForeignKey(Profile, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_photos/')
    is_primary = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        app_label = 'dating'
    
    def __str__(self):
        return f"Photo for {self.profile.user.username}"
