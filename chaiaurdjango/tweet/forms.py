from django import forms
from .models import Tweet 

class TweetForm(forms.ModelForm):
     class Meta:
          model = Tweet
          fields = ["text","photo"]

class Myform(forms.Form):
     name = forms.CharField( max_length=230, required=False)
     email = forms.EmailField( required=False)

