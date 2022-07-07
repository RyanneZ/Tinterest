from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Postcreated, Photo, Comments, User
import uuid
import boto3
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProfileForm, UserForm, PostcreatedForm

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

# show public user page
# @login_required
# def show_public_profile(request, user_id):
#   print(user_id)
#   print(request.user.id)
#   if user_id == request.user.id:
#     return redirect('/profile/')
#   else: 
#     return HttpResponse('here is public user profile')

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




@login_required
def posts_index(request):
  # posts = Postcreated.objects.filter(user=request.user)
  # to see all the posts created:
  posts = Postcreated.objects.order_by('?')
  return render(request, 'posts/index.html', { 'posts': posts })

@login_required
def posts_detail(request, post_id):
  comments = Comments.objects.filter(post = post_id)
  post = Postcreated.objects.get(id = post_id)
  return render(request, 'posts/detail.html', {'post': post, 'comments': comments})



  
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

def posts_edit(request, post_id):

  post = Postcreated.objects.get(id=post_id)
  form = PostcreatedForm(request.POST or None, request.FILES or None, instance = post)
  if form.is_valid():
    form.save()
    return redirect(f'/posts/{post.id}/')
  return render(request, 'posts/edit.html', {'post': post, 'form': form})


@login_required
def comments_create(request, post_id):

  Comments.objects.create(
    content = request.POST['content'],
    post = Postcreated.objects.get(id = post_id),
    user = User.objects.get(id = request.user.id)
  )

  return redirect(f'/posts/{post_id}/')


@login_required
def comments_delete(request, comment_id, post_id):
  post = Postcreated.objects.get(id = post_id),
  Comments.objects.get(id=comment_id).delete()
  return redirect(f'/posts/{post_id}/')


def search_posts(request):
  if request.method == 'POST':
    searched = request.POST['searched']
    posts = Postcreated.objects.filter(title__contains=searched,tags__contains=searched)
    return render(request, 'search.html', {'searched': searched, 'posts': posts})
  else:
    return render(request, 'search.html')
















