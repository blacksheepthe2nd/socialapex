# fix_middleware.py
middleware_code = '''# socialapex/middleware.py
from django.shortcuts import render

class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if user has access via cookie
        has_access = request.COOKIES.get('site_access') == 'true'
        
        # URLs that are always allowed (admin, static files, login POST, etc.)
        public_urls = [
            '/admin/', 
            '/static/', 
            '/media/',
            '/dating/login/'  # Allow login page and login POST requests
        ]
        
        # If no access and not a public URL, show maintenance page
        if not has_access and not any(request.path.startswith(url) for url in public_urls):
            return render(request, 'maintenance.html')
        
        return self.get_response(request)
'''

with open('socialapex/middleware.py', 'w', encoding='utf-8') as f:
    f.write(middleware_code)

print("✅ Updated middleware to allow login requests")