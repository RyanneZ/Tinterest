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

@login_required
def showProfile(request):
  
    return render(request, 'profile.html') 

S3_BASE_URL = "https://s3-website.ca-central-1.amazonaws.com"
BUCKET = "catcollector-ryanne"

class PostcreatedCreate(LoginRequiredMixin, CreateView):
  model = Postcreated
  fields = '__all__'
  success_url = '/profile'

  def __str__(self):
    return self.title
    

  def form_valid(self, form):
    form.instance.user = self.request.user
    print(self.object.id)
    return super().form_valid(form)

  
    
  
  # def form_valid(self, form):
  #   response = super().form_valid(form) # saves object
  #   print(self.object.id)
  #   return response, self.object.id




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







