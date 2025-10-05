#!/bin/bash 
set -e 
 
echo "=== Apex Social Final Deployment ===" 
 
"# Apply migrations" 
echo "Applying migrations..." 
python manage.py migrate 
 
"# Create essential data" 
echo "Creating essential data..." 
"from django.contrib.auth.models import User" 
"from dating.models import Profile, Interest" 
 
"# Create test user" 
"user, created = User.objects.get_or_create(" 
"    username='test'," 
"    defaults={'email': 'test@example.com'}" 
")" 
"if created:" 
"    user.set_password('test123')" 
"    user.save()" 
"    print('Test user created')" 
 
"# Create profile" 
"if not hasattr(user, 'profile'):" 
"    Profile.objects.create(" 
"        user=user," 
"        bio='Welcome to Apex Social dating community.'," 
"        location='Apex City'" 
"    )" 
"    print('Test user profile created')" 
 
"# Create interests" 
"interests = ['Travel', 'Music', 'Art', 'Technology', 'Sports', 'Food']" 
"for interest in interests:" 
"    Interest.objects.get_or_create(name=interest)" 
"print('Sample interests created')" 
 
"# Collect static files" 
echo "Collecting static files..." 
python manage.py collectstatic --noinput 
 
"# Start the server" 
echo "Starting Apex Social..." 
exec gunicorn socialapex.wsgi:application --bind 0.0.0.0:\$PORT 
