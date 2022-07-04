from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Postcreated, Photo 
import uuid
import boto3
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProfileForm, UserForm

#Profile

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from django.contrib import messages





# Define the welcome view (signup/login)
def welcome(request):
  return render(request, 'welcome.html')
 
# Define the signup view 
def signup(request):
  return render(request, 'signup.html')
 
# Define the home view
def home(request):
  print(request.user)
  return render(request, 'home.html')

#Oauth sign-up 
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request,user)
      return redirect('home')
    else: 
      error_message = 'Invalid sign up- try again'
  form = UserCreationForm()
  context = {'form':form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



# show profile page
@login_required
def showProfile(request):
  posts = Postcreated.objects.filter(user=request.user.id)
  return render(request,'profile.html', {'posts': posts}) 


#renders update profile page 
@login_required
def profile_edit(request):
    print(request.user.id)
    profile_form = ProfileForm()
    user_form = UserForm()
    return render(request, 'editprofile.html', {'profile_form': profile_form, 'user_form': user_form
    }) 


# extended profile update 
@login_required
def update_profile(request, user_id):
    user = User.objects.get(id=user_id)
    user.username = request.POST['username']
    user.profile.about = request.POST['about']
    user.profile.website = request.POST['website']
    user.save()
    return redirect('/profile/')




class PostcreatedCreate(LoginRequiredMixin, CreateView):
  model = Postcreated
  fields = '__all__'
  success_url = '/profile/'
  def __str__(self):
    return self.title


  
    
 
#amazon photo uplode:
S3_BASE_URL = "https://s3.us-east-2.amazonaws.com/"
BUCKET = 'catcollector-tatyana-1984'




@login_required
def posts_index(request):
  posts = Postcreated.objects.filter(user=request.user)
  return render(request, 'posts/index.html', { 'posts': posts })

@login_required
def posts_detail(request, post_id):
  post = Postcreated.objects.get(id = post_id)
  return render(request, 'posts/detail.html', {'post': post})



class PostcreatedUpdate(LoginRequiredMixin, UpdateView):
  model = Postcreated
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'
  
class PostcreatedDelete(LoginRequiredMixin, DeleteView):
  model = Postcreated
  success_url = '/posts/'


def new_post(request):
  return render(request, 'posts/new.html', {})

def posts_create(request):
  post = Postcreated.objects.create(
    image=request.FILES.get('image',None),
    title=request.POST['title'],
    description=request.POST['description'],
    tags=request.POST['tags'],
    user = request.user,
    
  )
  return redirect(f'/posts/{post.id}/')





