import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialapex.settings')
django.setup()

from django.db import connection
from django.contrib.auth.models import User

print("=== Database Verification ===")

# Check database file
db_path = 'db.sqlite3'
if os.path.exists(db_path):
    size = os.path.getsize(db_path)
    print(f"✅ Database file: {db_path} ({size} bytes)")

# Check tables
with connection.cursor() as cursor:
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cursor.fetchall()]
    print(f"✅ Found {len(tables)} tables:")
    for table in tables:
        print(f"  - {table}")

# Create test user
try:
    User.objects.filter(username='test').delete()
    user = User.objects.create_user('test', 'test@example.com', 'test123')
    print(f"✅ Test user created: {user.username}")
    
    user_count = User.objects.count()
    print(f"✅ Total users: {user_count}")
    
except Exception as e:
    print(f"❌ Error: {e}")
