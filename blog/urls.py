"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Register.views import view, ciew, prof
from news.views import Post,details
#from post import details
from django.conf.urls.static import static
from django.conf import settings

app_name='awwal'


    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', view),
    path('home/', Post, {'url':'home'},name='home'), 
    path('&:*+(^ent/', Post, {'url':'ent'},name='ent'), 
    path('_^¢€Π£ad/', Post,  {'url':'ad'}), 
    path('_£||•÷_sport/', Post, {'url':'sport'}, name='sport'), 
    path('¢ΠΠ¢\politics/', Post, {'url':'politics'},name='politics'), 
    path('front/', Post, {'url':'front'}), 
    path('login/', ciew), 
    path('prof/', prof), 
    path('√¢€£|•÷_×=_<slug:slug>/', details,  name ='details'), 
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    