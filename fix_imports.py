# Fix script for dj_database_url import 
import sys 
 
# Read current settings 
with open('socialapex/settings.py', 'r') as f: 
    content = f.read() 
 
# Add import at top if missing 
if 'import dj_database_url' not in content.split('\n')[2]: 
    content = content.replace('import os', 'import os\\nimport dj_database_url', 1) 
 
# Remove duplicate import from DATABASE_URL block 
import re 
content = re.sub(r\"if 'DATABASE_URL' in os\.environ:\\s*\\n\\s*import dj_database_url\", \"if 'DATABASE_URL' in os.environ:\", content) 
 
# Write fixed content 
with open('socialapex/settings.py', 'w') as f: 
    f.write(content) 
 
print('Fixed imports successfully') 
