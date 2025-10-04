import os
import django
import sqlite3

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialapex.settings')
django.setup()

from django.db import connection
from django.contrib.auth.models import User

print("=== Database Debug Information ===")

# Check database file
db_path = 'db.sqlite3'
if os.path.exists(db_path):
    size = os.path.getsize(db_path)
    print(f"✅ Database file exists: {db_path} ({size} bytes)")
else:
    print(f"❌ Database file does not exist: {db_path}")

# Check tables using direct SQLite connection
try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # List all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    if tables:
        print("✅ Tables in database:")
        for table in tables:
            print(f"  - {table[0]}")
    else:
        print("❌ No tables found in database")
    
    conn.close()
except Exception as e:
    print(f"❌ Error accessing database: {e}")

print("\n=== Django Database Check ===")
try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        django_tables = cursor.fetchall()
        print(f"Django can see {len(django_tables)} tables")
        
        # Check if auth_user exists
        if ('auth_user',) in django_tables:
            print("✅ auth_user table exists")
            cursor.execute("SELECT COUNT(*) FROM auth_user;")
            user_count = cursor.fetchone()[0]
            print(f"✅ Users in auth_user: {user_count}")
        else:
            print("❌ auth_user table does not exist")
            
except Exception as e:
    print(f"❌ Django database error: {e}")

print("\n=== Migration Status ===")
from django.core.management import execute_from_command_line
execute_from_command_line(['manage.py', 'showmigrations'])
