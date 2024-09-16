from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    bio = models.TextField(max_length=400, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="hi my name is description")
    categories = models.ManyToManyField(Category, related_name='products',null=True,blank=True)
    profile = models.OneToOneField(Profile, related_name='product', on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE,null=True,blank=True)
    rating = models.IntegerField(default=0)
    comment = models.TextField(default="this is deault comment ")

    def __str__(self):
        return f"Review for {self.product.name}"
