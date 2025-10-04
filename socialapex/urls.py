from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dating/', include('dating.urls')),
    path('', views.index, name='home'),  # Serve Apex Social landing page at root
    path('', include('main.urls')),  # Include main app URLs
]
