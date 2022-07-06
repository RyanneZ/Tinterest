from os import F_OK
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from platformdirs import user_cache_dir, user_log_dir
from .models import Postcreated, Photo, Savedpost
import uuid
import boto3
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# from .forms import ProfileForm, UserForm

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
  
  savedposts = Savedpost.objects.filter(user = request.user)
  # print(savedposts.post)
  # iterate over savedposts grab the post.img and put that into a new list
  return render(request,'profile.html', {'posts': posts, 'savedposts': savedposts}) 



# show public user page
@login_required
def show_public_profile(request, user_id):
  print(user_id)
  print(request.user.id)
  user = User.objects.get(id=user_id)
  posts = Postcreated.objects.filter(user=user_id)
  if user_id == request.user.id:
    return redirect('/profile/')
  else:
   return render(request, 'public-user-profile.html', {'user': user, 'posts': posts})


#renders update profile page 
@login_required
def profile_edit(request):
    print(request.user.id)
    user = User.objects.get(id=request.user.id)
    return render(request, 'editprofile.html', {'user': user
    }) 


# extended profile update 
@login_required
def update_profile(request, user_id):
    user = User.objects.get(id=user_id)
    user.username = request.POST['username']
    user.profile.about = request.POST['about']
    user.profile.website = request.POST['website']
    # user.profile.image = request.POST['image']
    user.save()
    return redirect('/profile/')




class PostcreatedCreate(LoginRequiredMixin, CreateView):
  model = Postcreated
  fields = '__all__'
  success_url = '/profile'
  def __str__(self):
    return self.title
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

  
    
 
#amazon photo uplode:
S3_BASE_URL = "https://s3.us-east-2.amazonaws.com/"
BUCKET = 'catcollector-tatyana-1984'

@login_required
def add_photo(request):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    #store the file in s3
    filename = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
     s3 = boto3.client('s3')
     s3.upload_fileobj(photo_file, BUCKET, filename)
    #create a DB entry in photo table with url
     url = f"{S3_BASE_URL}{BUCKET}/{filename}"
     Photo.objects.create(url=url)
     return redirect('/profile')
    except: 
      return HttpResponse("something went wrong with uploading to amazon s3")
  else:
    return HttpResponse("no photos were received")

# this will be the home feed
@login_required
def posts_index(request):
  # posts = Postcreated.objects.filter(user=request.user)
  # to see all the posts created:
  posts = Postcreated.objects.order_by('?')
  return render(request, 'posts/index.html', { 'posts': posts })

# show detail page (if not user's detail page, show readDetail)
@login_required
def posts_detail(request, post_id):
  post = Postcreated.objects.get(id = post_id)
# if user id = logged in user show detail page with "edit btn", if not show detail page with "save btn"
  if request.user == post.user:
    print(request.user)
    return render(request, 'posts/detail.html', {'post': post} )
  else:
    return render(request, 'posts/readDetail.html', {'post': post} )




class PostcreatedUpdate(LoginRequiredMixin, UpdateView):
  model = Postcreated
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'
  
class PostcreatedDelete(LoginRequiredMixin, DeleteView):
  model = Postcreated
  success_url = '/posts/'




# save post
def save_post(request, post_id):
  Savedpost.objects.create(
    post = Postcreated.objects.get(id = post_id),
    user = User.objects.get(id = request.user.id)
  )
  
  return redirect('/profile/')






