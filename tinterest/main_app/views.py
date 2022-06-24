from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Postcreated, Photo
import uuid
import boto3


# Add the following import
from django.http import HttpResponse

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

def showProfile(request):
  return render(request, 'profile.html') 

class PostcreatedCreate(CreateView):
  model = Postcreated
  fields = '__all__'
  success_url = '/profile'

  def __str__(self):
    return self.title
  
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)


#amazon photo uplode:
S3_BASE_URL = "https://s3-website.ca-central-1.amazonaws.com"
BUCKET = "catcollector-ryanne"

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

def posts_index(request):
  posts = Postcreated.objects.all()
  return render(request, 'posts/index.html', { 'posts': posts })

def posts_detail(request, post_id):
  post = Postcreated.objects.get(id = post_id)
  return render(request, 'posts/detail.html', {'post': post})



class PostcreatedUpdate(UpdateView):
  model = Postcreated
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = '__all__'
  
class PostcreatedDelete(DeleteView):
  model = Postcreated
  success_url = '/posts/'