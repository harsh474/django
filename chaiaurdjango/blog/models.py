from django.db import models
from django.utils import timezone

# Create your models here.
class Chai(models.Model): 
     CHAI_TYPE_CHOICE = [
          ('ML','MASALA'),
          ('PL','PLAIN'),
          ('GI','GINGER'),
          ('EL','ELIACHI'),
     ]
     name = models.CharField(max_length=50) 
     image = models.ImageField(upload_to='chais/')
     date_added = models.DateTimeField(default=timezone.now())
     type = models.CharField(max_length = 2,choices = CHAI_TYPE_CHOICE)
     discription = models.TextField(default='this feild is empty')
     price = models.IntegerField(default='9')
     total_price = models.IntegerField(default='9')
     def __str__(self):
         return self.name
