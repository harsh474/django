
from django.urls import path,include
from  . import views
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [ 
                
                path('',views.tweet_list,name="tweet_list"),
               #  path('', views.tweet,name = 'tweet'),
                path('tweet_create/',views.tweet_create,name="tweet_create"),
                path('<int:tweet_id> /tweet_edit/',views.tweet_edit,name="tweet_edit"),
                path('<int:tweet_id>/tweet_delete/',views.tweet_delete,name="tweet_delete"),    
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
