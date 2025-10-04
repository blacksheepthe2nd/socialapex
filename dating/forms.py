from django import forms
from .models import Profile, ProfilePhoto, Interest
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'location', 'tagline', 'about', 'interests']
        widgets = {
            'about': forms.Textarea(attrs={'rows': 4}),
            'interests': forms.CheckboxSelectMultiple(),
        }

class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = ProfilePhoto
        fields = ['image', 'is_primary']
