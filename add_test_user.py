# add_test_user.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialapex.settings')
django.setup()

from django.contrib.auth.models import User

# Create test user if it doesn't exist
try:
    user = User.objects.get(username='test')
    print("✅ Test user already exists")
except User.DoesNotExist:
    user = User.objects.create_user('test', password='test123')
    print("✅ Created test user: test / test123")