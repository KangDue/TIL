from django.forms import forms
from .models import Article,Comment

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        #fields = '__all__'#("",)
        exclude = ('user','like_users')
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('user','article') # form에 받을 필요 없음.
        