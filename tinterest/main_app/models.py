from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Postcreated(models.Model):
  image = models.ImageField(null=False, blank=False)
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  tags = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.description

class Photo(models.Model):
 
  picture = models.FileField(upload_to='media/')
  post = models.ForeignKey(Postcreated(), on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
 
    description = models.CharField(max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed
    