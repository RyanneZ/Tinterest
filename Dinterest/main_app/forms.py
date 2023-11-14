from django.forms import ModelForm
from .models import Profile, User, Postcreated
from django import forms

class ProfileForm(ModelForm): 
    class Meta: 
        model = Profile
        fields = ['image', 'about', 'website']
        
       
class UserForm(ModelForm): 
    class Meta: 
        model = User
        fields = ['username']

class PostcreatedForm(ModelForm):
    class Meta:
        model = Postcreated
        fields = ['image', 'title', 'description', 'tags']