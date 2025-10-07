from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login, authenticate 
from django.contrib import messages 
from .models import Profile 
 
@csrf_exempt
def login_view(request): 
    if request.method == 'POST': 
        username = request.POST.get('username', '') 
        password = request.POST.get('password', '') 
 
        user = authenticate(request, username=username, password=password) 
 
        if user is not None: 
            login(request, user) 
            return redirect('/dating/dashboard/') 
        else: 
            messages.error(request, 'Invalid credentials') 
 
    return render(request, 'login.html') 
 
@login_required 
def dashboard(request): 
    return render(request, 'dashboard.html') 
 
@login_required 
def individual_view(request): 
    profiles = Profile.objects.all().order_by('?') 
    return render(request, 'individual_dashboard.html', {'profiles': profiles}) 
 
@login_required 
def grid_view(request): 
    profiles = Profile.objects.all().order_by('?') 
    return render(request, 'grid_dashboard.html', {'profiles': profiles}) 
 
@login_required 
def profile_detail(request, pk): 
    profile = get_object_or_404(Profile, pk=pk) 
    return render(request, 'profile.html', {'profile': profile}) 
 
@login_required 
def create_profile(request): 
    from django.http import HttpResponse 
    return HttpResponse("Create profile page - coming soon") 
 
@login_required 
def edit_profile(request): 
    from django.http import HttpResponse 
    return HttpResponse("Edit profile page - coming soon") 
 
def register_view(request): 
    return render(request, 'registration/register.html') 
