
from django.urls import path
from  . import views
urlpatterns = [
       path('', views.blog ,name ='blog'),
       path('sport', views.sportblog ,name ='sportblog'),
       path('all-blog',views.all_blog,name= "all_blog"), 
       path('blog_discription/<int:id>/',views.blog_discription,name = "blog_discription" )
]
