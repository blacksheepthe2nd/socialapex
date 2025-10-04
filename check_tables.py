import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialapex.settings')
django.setup()

from django.db import connection

print("=== Checking All Tables ===")
with connection.cursor() as cursor:
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cursor.fetchall()]
    print(f"Total tables: {len(tables)}")
    
    essential_tables = [
        'auth_user',
        'django_session', 
        'django_migrations',
        'dating_profile',
        'dating_interest',
        'dating_profile_interests'
    ]
    
    for table in essential_tables:
        if table in tables:
            print(f"✅ {table}")
        else:
            print(f"❌ {table} - MISSING")
