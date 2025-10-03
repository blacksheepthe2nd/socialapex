from django.contrib import admin 
from .models import UserProfile, Photo, Like, Match, Message 
 
admin.site.register(UserProfile) 
admin.site.register(Photo) 
admin.site.register(Like) 
admin.site.register(Match) 
admin.site.register(Message) 
