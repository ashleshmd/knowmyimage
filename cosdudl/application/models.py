from django.db import models

# Create your models here.

import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

class Profile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    profile_image = models.FileField(upload_to='application/images',null=True,blank=True)
    usn = models.CharField(max_length=20,default='')
    branch = models.CharField(max_length=20,default='')
    section = models.CharField(max_length=20,default='')
    locality = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.user.username
class Profile_image(models.Model):
    name =models.CharField(max_length=50)
    image = models.ImageField(upload_to='application/images',default='')