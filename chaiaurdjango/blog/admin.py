from django.contrib import admin
from .models import Profile,Product
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
# admin.site.register(Chai)

class ProfileInline(admin.StackedInline) : 
     model = Profile
     can_delete = False 
     verbose_name_plural = 'Profiles'   

class ProfileAdmin(admin.ModelAdmin): 
     inlines = [ProfileInline]



admin.site.register(Product,ProfileAdmin)
admin.site.register(Profile)
