from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Product(models.Model): 
      name = models.CharField(max_length=30)
      email = models.CharField(max_length=30)


class Profile(models.Model):
     bio = models.TextField(max_length=400)
     birth_date = models.DateField(null = True , blank=True) 
     product = models.OneToOneField(Product,related_name ="Product", on_delete=models.CASCADE,default=1)


