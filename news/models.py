from django.db import models
from django.urls import reverse

cat=(('Entertainment', 'Entertainment'), ('Sport','Sport') , ('politics','politics'), ('fashion','fashion'), ('technology', 'technology'), ( 'bussiness', 'bussiness'), )
# Create your models here.
#class title(forms.Form):
#    category=forms.CharField( label='category',  max_length=15, required=False, widget=forms.Select(choices=cat))
#    head=forms.CharField(label='title',  required=False,  max_length=30)
#    Post=forms.CharField(label='Body',required=False,   widget=forms.Textarea)
    
class title(models.Model):
    category=models.CharField(max_length=30, choices=cat)
    Date=models.DateTimeField(null=True, auto_now_add= True)
    slug=models.SlugField(unique=True)
    head=models.CharField(max_length=30)
    Image=models.ImageField(upload_to='images/')
    Post=models.TextField()
    Views=models.IntegerField(default=0,blank=True,null=True)
    
    def __str__(self):
        return self.head
        
    class Meta: 
        ordering = ['Date']
        
class Image(models.Model):
    post=models.ForeignKey(title, null=True,blank=True,related_name='post',on_delete=models.CASCADE)
    description=models.CharField(max_length=500,null=True,blank=True)
    image=models.ImageField(upload_to='images/',blank=True,null=True)        
              
    def __str__(self):
        return 'Image'

class Comment(models.Model):
    Part=models.ForeignKey(title,    related_name='comments', on_delete=models.CASCADE)
    Date=models.DateTimeField(null=True, auto_now_add= True)
    name=models.CharField(max_length=25)
    body=models.TextField()
    
    class Meta:
        ordering=['Date']
    
    def __str__(self):
        return self.body
    

