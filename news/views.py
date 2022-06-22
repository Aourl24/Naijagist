from django.shortcuts import render
from .models import title, Comment
#from news.models import title, Comment
from mform import fost
# Create your views here.
#from forms import visitor
from requests.exceptions import ConnectionError

import requests

def Post(request, url):
    Post=title.objects.all()
    username='Aourl24';
    #add='https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=8c0b2d7b2f9443b085a47683cbcb3028'
     # try:
    
    #except ConnectionError:
#        response='no response'
#        con=response.json()
    
    
    #print(con)
    if url== 'home':
        add='https://newsapi.org/v2/top-headlines?country=ng&apiKey=8c0b2d7b2f9443b085a47683cbcb3028'
        a='post.html'
    elif url=='ent':
        add='https://newsapi.org/v2/top-headlines?country=ng&category=entertainment&apiKey=8c0b2d7b2f9443b085a47683cbcb3028 '
        a='ent.html'
    
    elif url=='ad':
        a='nadmin.html'
    elif url=='sport':
        add='https://newsapi.org/v2/top-headlines?country=ng&category=sports&apiKey=8c0b2d7b2f9443b085a47683cbcb3028 '
        a='sport.html'
    elif url=='politics':
        add='https://newsapi.org/v2/top-headlines?country=ng&category=business&apiKey=8c0b2d7b2f9443b085a47683cbcb3028 '
        a='politics.html'
    elif url=='front':
        a='front.html'
        
        
    response=requests.get(add)
    con=response.json()
    return render(request ,a,  {'Post':Post,'con':con})
    

count=[]      
def details(request, slug):
    post=title.objects.get(slug=slug)
    sess=request.session.session_key
    
    #print(sess)
    #print(count)
    if sess is None:
        sess=request.path_info
    sess=sess+slug
    if sess in count:
        pass
    else:
        post.Views=post.Views + 1
        count.append(sess)
    post.save()
    #Comments=post.comments.all()
    form=fost() 
    if request.method =='POST':
        form=fost(request.POST)
        if form.is_valid():
            c=form.save(commit=False)
            k=form['name'].value()
            d=form['body'].value()
            print(k + ' ' + d)
            c.Part=post
            c.save()
            
            
        
    return render(request, 'details.html', {'post':post, 'form':form} )
       
    
