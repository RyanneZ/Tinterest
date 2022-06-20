from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  # path('tinterest/', views.tinterest_index, name='index')
  # path('tintrest')
]