

from django.contrib import admin

# Register your models here.
from .models import Postcreated, Photo, Profile

# Register your models here
admin.site.register(Postcreated)
admin.site.register(Photo)
admin.site.register(Profile)