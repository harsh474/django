from django.shortcuts import render
from django.http import HttpResponse
from .models import Chai
# Create your views here.
def blog(request): 
     return HttpResponse("this is a blog app")

def sportblog(request): 
     return HttpResponse("this is a sportblog app")
def all_blog(request):
     blog ={ 
        'title':"t1", 
        'content':"c1"
     }
     blog2 ={ 
        'title':"t1", 
        'content':"c1"
     }
     posts = [
        {'title': 'First Post', 'author': 'Author 1'},
        {'title': 'Second Post', 'author': 'Author 2'},
    ]
     chais = Chai.objects.all()
     context = {'posts': chais}
     
     return render(request,"blog/all_blog.html",context)


def blog_discription(request, id): 
    chai = Chai.objects.get(id=id)  # Pass id as a keyword argument
    chai.delete()
    return HttpResponse("chai with id is deleted")
#   return render(request, "blog/blog_discription.html", {"chai": chai})
