# create_test_user.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialapex.settings')
django.setup()

from django.contrib.auth.models import User

# Delete existing test user if it exists
User.objects.filter(username='test').delete()

# Create new test user
user = User.objects.create_user('test', password='test123')
user.save()

print("✅ Created test user: test / test123")