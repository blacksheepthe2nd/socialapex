from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Profile, ProfilePhoto, Interest
from .forms import UserForm, ProfileForm, ProfilePhotoForm

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
    return render(request, 'user_profile.html', {'profile': profile})

@login_required
def create_profile(request):
    if hasattr(request.user, 'profile'):
        return redirect('edit_profile')

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            profile_form.save_m2m()
            messages.success(request, 'Profile created successfully!')
            return redirect('dashboard')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm()

    return render(request, 'create_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def edit_profile(request):
    if not hasattr(request.user, 'profile'):
        return redirect('create_profile')

    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
