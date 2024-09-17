
from django.urls import path,include
from  . import views
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
               
                path('', views.tweet,name = 'tweet'),
                path('form', views.my_form_view,name = 'tweet'),
                
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
