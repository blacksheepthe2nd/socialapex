# update_middleware.py
with open('socialapex/settings.py', 'r') as f:
    content = f.read()

# Add the middleware after SecurityMiddleware
new_content = content.replace(
    "MIDDLEWARE = [\n    'django.middleware.security.SecurityMiddleware',",
    "MIDDLEWARE = [\n    'django.middleware.security.SecurityMiddleware',\n    'socialapex.middleware.MaintenanceMiddleware',"
)

with open('socialapex/settings.py', 'w') as f:
    f.write(new_content)

print('✅ Updated settings.py with MaintenanceMiddleware')