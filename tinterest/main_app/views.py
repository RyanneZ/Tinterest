from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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

