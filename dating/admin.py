from django.contrib import admin
from .models import Profile, Interest  # Removed ProfilePhoto

admin.site.register(Profile)
admin.site.register(Interest)
# admin.site.register(ProfilePhoto)  # Commented out
