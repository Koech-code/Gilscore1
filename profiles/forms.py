from django import forms
from accounts.models import User
from django.forms import ModelChoiceField

from .models import Profile
class UserProfileForm(forms.ModelForm):
    location = forms.CharField(required=False)
    bio = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    clubimage = forms.ImageField(required=False)
    Team1 = forms.ImageField(required=False)
    Afcon = forms.ImageField(required=False)
    Baseball = forms.ImageField(required=False)
    Bundesliga = forms.ImageField(required=False)
    Europa = forms.ImageField(required=False)
    Formula1 = forms.ImageField(required=False)
    Laliga = forms.ImageField(required=False)
    NBA = forms.ImageField(required=False)
    NFL = forms.ImageField(required=False)
    Worldcup = forms.ImageField(required=False)
    Team = forms.ImageField(required=False)
    Team = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email',]


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.CharField(required=False)
    class Meta:
        model = Profile
        fields = [ 
            "user",
            "first_name",
            "last_name",
            "email",
            "image",
            # "club",
            "club_icon",
            "bio",
            "location",
            "followers",
            
            ]


class ProfileBasicForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email_address = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    location = forms.CharField(required=False)
    bio = forms.CharField(required=False)
    clubimage = forms.ImageField(required=False)
