#!/bin/bash
set -e

echo "=== Apex Social Final Deployment ==="

# 1. Apply ALL migrations (no more missing tables)
echo "Applying migrations..."
python manage.py migrate

# 2. Create essential data (no more empty databases)
echo "Creating essential data..."
python manage.py shell -c "
from django.contrib.auth.models import User
from dating.models import Profile, Interest

# Create test user if doesn't exist
user, created = User.objects.get_or_create(
    username='test',
    defaults={'email': 'test@example.com'}
)
if created:
    user.set_password('test123')
    user.save()
    print('✅ Test user created')

# Create profile for test user if doesn't exist
if not hasattr(user, 'profile'):
    Profile.objects.create(
        user=user,
        bio='Welcome to Apex Social - your exclusive dating community.',
        location='Apex City'
    )
    print('✅ Test user profile created')

# Create some sample interests
interests = ['Travel', 'Music', 'Art', 'Technology', 'Sports', 'Food']
for interest in interests:
    Interest.objects.get_or_create(name=interest)
print('✅ Sample interests created')
"

# 3. Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# 4. Start the server
echo "Starting Apex Social..."
exec gunicorn socialapex.wsgi:application --bind 0.0.0.0:\$PORT
