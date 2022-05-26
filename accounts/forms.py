from django import forms
from whatsonzambia.models import CustomUser
from whatsonzambia.forms import CustomUserCreationForm
from phonenumber_field.modelfields import PhoneNumberField
from .models import Profile

class UserRegistrationForm(CustomUserCreationForm):
    fullname = forms.CharField(max_length=100)
    contact = PhoneNumberField()

    class Meta:
        model = CustomUser
        fields = ['email', 'fullname', 'contact', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    fullname = forms.CharField(max_length=100)
    contact = PhoneNumberField()

    class Meta:
        model = CustomUser
        fields = ['email', 'fullname', 'contact']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']