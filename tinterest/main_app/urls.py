from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.home, name='home'),
  path('welcome', views.welcome, name='welcome'),
  path('accounts/signup/', views.signup, name='signup'),
  
  #temperate profile url
  path('profile/', views.showProfile, name='profile'),
  path('profile/edit/', views.profile_edit, name='edit_profile'),
  path('profile/<int:user_id>/submit_update_form/', views.update_profile, name='update_profile'), # handle submission of edit form data
  path('posts/create',views.PostcreatedCreate.as_view(), name='posts_create'),
  path('posts/add_photo/', views.add_photo, name='add_photo'),
  path('posts/', views.posts_index, name='index'),
  path('posts/<int:post_id>/', views.posts_detail, name='detail'),
  path('posts/<int:pk>/update/', views.PostcreatedUpdate.as_view(), name='posts_update'),
  path('posts/<int:pk>/delete/', views.PostcreatedDelete.as_view(), name='posts_delete'),
  path('posts/<int:post_id>/comments/', views.comments_create, name='comments_create') 

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)