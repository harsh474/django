from django import forms
from .models import Tweet 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

class TweetForm(forms.ModelForm):
     class Meta:
          model = Tweet
          fields = ["text","photo"]


# through this we cant save our data into database
# class Myform(forms.Form):
#      name = forms.CharField( max_length=230, required=False)
#      email = forms.EmailField( required=False)

class Myform(forms.ModelForm):
      class Meta:
          model = Tweet
          fields = ["text","photo"]

class UserRegisterationForm(UserCreationForm): 
       email = forms.EmailField()
       class Meta:
            model = User 
            fields = ('username','email','password1','password2')