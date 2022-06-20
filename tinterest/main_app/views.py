from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  user = request.user
  print(user)
  return render(request, 'home.html', { 'user':user })



