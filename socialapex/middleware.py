# socialapex/middleware.py
from django.shortcuts import render

class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if user has access via cookie
        has_access = request.COOKIES.get('site_access') == 'true'
        
        # URLs that are always allowed
        public_urls = [
            '/admin/', 
            '/static/', 
            '/media/',
            '/dating/login/',  # Allow login page
            '/favicon.ico'
        ]
        
        # Allow authenticated users (they passed login)
        user_authenticated = request.user.is_authenticated
        
        # If no access, not authenticated, and not a public URL, show maintenance page
        if not has_access and not user_authenticated and not any(request.path.startswith(url) for url in public_urls):
            return render(request, 'maintenance.html')
        
        return self.get_response(request)
