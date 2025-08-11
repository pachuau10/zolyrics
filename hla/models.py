from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=225)
    phuahtu = models.CharField(max_length=255,)
    satu = models.CharField(max_length=255,)
    desc = models.TextField()
    img = CloudinaryField('image', 
                         folder='thlalak/',
                         null=True, blank=True)
    views = models.PositiveIntegerField(default=0) 
   


    def __str__(self):
        return self.name
    

class Req(models.Model):
    req = models.TextField()


    def __str__(self):
        return self.req
       
