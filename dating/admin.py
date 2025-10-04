from django.contrib import admin
from .models import Profile, ProfilePhoto, Interest

class ProfilePhotoInline(admin.TabularInline):
    model = ProfilePhoto
    extra = 1

class InterestInline(admin.TabularInline):
    model = Profile.interests.through
    extra = 1

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'location', 'tagline', 'created_at']
    list_filter = ['age', 'location', 'created_at']
    search_fields = ['user__username', 'tagline', 'about']
    inlines = [ProfilePhotoInline, InterestInline]

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(ProfilePhoto)
class ProfilePhotoAdmin(admin.ModelAdmin):
    list_display = ['profile', 'image', 'is_primary', 'uploaded_at']
    list_filter = ['is_primary', 'uploaded_at']
