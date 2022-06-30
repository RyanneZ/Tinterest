from django.forms import ModelForm
from .models import Profile, User
from django import forms

# class ProfileForm(ModelForm): 
#     class Meta: 
#         model = Profile
#         fields = ['image', 'about', 'website']
        

# class ProfileForm(forms.Form): 
#     bio = forms.CharField(default="default value"), 
#     url = forms.URLField(label='Website', required=False)
      
    
class UserForm(ModelForm): 
    class Meta: 
        model = User
        fields = ['username']


class ProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False,
                             widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    about = forms.CharField(max_length=200, 
                            required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.URLField(required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    

    class Meta:
        model = Profile
        fields = ['image', 'about', 'website']


# class UserForm(ModelForm): 
#     username = forms.CharField(max_length=100,
#                                required=True,
#                                widget=forms.TextInput(attrs={'class': 'form-control'}))
#     class Meta: 
#         model = User
#         fields = ['username']