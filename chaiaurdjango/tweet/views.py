from django.shortcuts import render ,get_object_or_404 ,redirect
from django.http import HttpResponse 
from .models import Tweet 
from .forms import TweetForm ,UserRegisterationForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

def tweet(request): 
     # return HttpResponse("hi this is a tweet app")
     return render(request,'index.html')

def tweet_list(request): 
    tweets =  Tweet.objects.order_by('-created_at')
    return render(request,'tweet_list.html',{"tweets":tweets})


@login_required
def tweet_create(request): 
     if request.method == "POST":
         form = TweetForm(request.POST,request.FILES)
         if form.is_valid():
             tweet = form.save(commit=False)
             tweet.user = request.user
             tweet.save()
             return redirect('tweet_list')

     else:
          form  = TweetForm()
          return render(request,'tweet_form.html',{'form':form})
     

# @login_required
def tweet_edit(request,tweet_id):
     tweet = get_object_or_404(Tweet,pk=tweet_id,user = request.user)
     if request.method =="POST":
          form = TweetForm(request.POST,request.FILES,instance=tweet)
          if form.is_valid():
             tweet = form.save(commit=False)
             tweet.user = request.user
             tweet.save()
             return redirect('tweet_list')
     else:
          form  = TweetForm(instance=tweet)
          return render(request,'tweet_form.html',{'form':form})
# @login_required
def tweet_delete(request,tweet_id): 
     tweet  = get_object_or_404(Tweet,pk = tweet_id,user = request.user)     
     if request.method =="POST":
          tweet.delete()
          return redirect('tweet_list')
     else:  
          return render(request,'tweet_confirm_delete.html',{'tweet':tweet})




def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log in the user after registration
            return redirect('tweet_list')  # Redirect to home after successful registration
    else:
        form = UserRegisterationForm()
    
    return render(request, 'registration/register.html', {'form': form})