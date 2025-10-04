from django import forms
from django.contrib.auth.models import User
from .models import Profile, Interest

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=Interest.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'interests']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

# Remove ProfilePhotoForm for now
# class ProfilePhotoForm(forms.ModelForm):
#     class Meta:
#         model = ProfilePhoto
#         fields = ['image', 'is_primary']
