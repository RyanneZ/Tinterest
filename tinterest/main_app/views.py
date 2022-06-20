from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  user = request.user
  return render(request, 'home.html', {'user': user})

# def tinterest_index(request):
#   if request.user.is_authenticated:
#    return HttpResponse('<h1>you are logged in!</h1>')
#   else: 
#     return HttpResponse('<h1>you are not logged in!</h1>')

