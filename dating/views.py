from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q
from django.contrib.auth.models import User
from .models import UserProfile, Like, Match
from .forms import CustomUserCreationForm, UserProfileForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('create_profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def create_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'create_profile.html', {'form': form})

@login_required
def dashboard(request):
    # Skip profile check for superusers/staff
    if not request.user.is_superuser and not request.user.is_staff:
        try:
            request.user.userprofile
        except UserProfile.DoesNotExist:
            return redirect('create_profile')

    liked_user_ids = Like.objects.filter(from_user=request.user).values_list('to_user_id', flat=True)
    profiles = UserProfile.objects.exclude(
        Q(user=request.user) | Q(user_id__in=liked_user_ids)
    )[:20]

    return render(request, 'dashboard.html', {'profiles': profiles})

@login_required
def profiles_grid(request):
    # Skip profile check for superusers/staff
    if not request.user.is_superuser and not request.user.is_staff:
        try:
            request.user.userprofile
        except UserProfile.DoesNotExist:
            return redirect('create_profile')

    profiles = UserProfile.objects.exclude(user=request.user)
    return render(request, 'profiles_grid.html', {'profiles': profiles})

@login_required
def profile_detail(request, user_id):
    # Skip profile check for superusers/staff
    if not request.user.is_superuser and not request.user.is_staff:
        try:
            request.user.userprofile
        except UserProfile.DoesNotExist:
            return redirect('create_profile')

    profile = get_object_or_404(UserProfile, user_id=user_id)
    return render(request, 'profile.html', {'profile': profile})

@login_required
def like_profile(request, user_id):
    # Skip profile check for superusers/staff
    if not request.user.is_superuser and not request.user.is_staff:
        try:
            request.user.userprofile
        except UserProfile.DoesNotExist:
            return redirect('create_profile')

    if request.method == 'POST':
        to_user = get_object_or_404(User, id=user_id)
        like, created = Like.objects.get_or_create(
            from_user=request.user,
            to_user=to_user
        )

        mutual_like = Like.objects.filter(
            from_user=to_user,
            to_user=request.user
        ).exists()

        if mutual_like:
            match, created = Match.objects.get_or_create()
            match.users.add(request.user, to_user)

    return redirect('dashboard')

@login_required
def matches(request):
    # Skip profile check for superusers/staff
    if not request.user.is_superuser and not request.user.is_staff:
        try:
            request.user.userprofile
        except UserProfile.DoesNotExist:
            return redirect('create_profile')

    user_matches = Match.objects.filter(users=request.user)
    return render(request, 'matches.html', {'matches': user_matches})