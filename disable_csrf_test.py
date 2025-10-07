# disable_csrf_test.py
with open('dating/views.py', 'r') as f:
    content = f.read()

# Add csrf_exempt to the login view
from django.views.decorators.csrf import csrf_exempt

if 'def login_view(request):' in content and '@csrf_exempt' not in content:
    content = content.replace(
        'def login_view(request):',
        '@csrf_exempt\ndef login_view(request):'
    )

with open('dating/views.py', 'w') as f:
    f.write(content)

print("✅ Temporarily disabled CSRF for login view for testing")