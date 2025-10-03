from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from .models import UserProfile, Photo 
 
class CustomUserCreationForm(UserCreationForm): 
    email = forms.EmailField(required=True) 
 
    class Meta: 
        model = User 
        fields = ('username', 'email', 'password1', 'password2') 
 
class UserProfileForm(forms.ModelForm): 
    class Meta: 
        model = UserProfile 
        fields = ['bio', 'age', 'gender', 'location', 'profile_picture'] 
        widgets = { 
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about yourself...'}), 
            'age': forms.NumberInput(attrs={'min': 18, 'max': 100}), 
        } 
 
class PhotoForm(forms.ModelForm): 
    class Meta: 
        model = Photo 
        fields = ['image'] 
