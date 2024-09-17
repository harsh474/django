from django import forms
from .models import Tweet 

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
