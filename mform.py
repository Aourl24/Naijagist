from news.models import Comment
from django import forms

class fost(forms.ModelForm):
    body=forms.CharField(widget=forms.Textarea(attrs={'class':'text'}))
    class Meta:
        model= Comment
        fields=('name', 'body', )
       