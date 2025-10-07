# fix_hosts.py
with open('socialapex/settings.py', 'r') as f:
    content = f.read()

# Update ALLOWED_HOSTS for both domains
content = content.replace(
    "ALLOWED_HOSTS = []", 
    "ALLOWED_HOSTS = ['socialapex.live', 'www.socialapex.live', 'localhost', '127.0.0.1']"
)

# Update Railway section too
content = content.replace(
    "if 'RAILWAY_STATIC_URL' in os.environ:\n    ALLOWED_HOSTS = ['*']\n    DEBUG = False",
    "if 'RAILWAY_STATIC_URL' in os.environ:\n    ALLOWED_HOSTS = ['socialapex.live', 'www.socialapex.live', '.railway.app', 'localhost', '127.0.0.1']\n    DEBUG = False"
)

with open('socialapex/settings.py', 'w') as f:
    f.write(content)

print('✅ Updated ALLOWED_HOSTS for socialapex.live and www.socialapex.live')