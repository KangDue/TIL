from multiprocessing import context
from symbol import except_clause
from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content
    
    
from django import forms
from .models import Article,Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('user',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('article','uesr',)
        
from django.contrib import admin
from .models import Article,Comment

admin.site.register(Article)
admin.site.register(Comment)

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns=[
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/update/',views.update,name='update'),
    path('<int:pk>/comments',views.comments_create,name='comments'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/',views.comments_delete,name='comment_delete')
]

from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods,require_POST,require_safe
from django.contrib.auth.decorators import login_required
from .models import Article,Comment
from .forms import ArticleForm,CommentForm

@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request,'articles/index.html',context)

@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm()
    context={
        'form':form
    }
    return render(request,'articles/create.html',context)


@require_safe
def detail(request,pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article':article,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request,'articles/detail.html',context)

@require_POST
def delete(request,pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail',article.pk)


@login_required
@require_http_methods(['GET','POST'])
def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST,instance = article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail',article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'form':form,
            'article':article
        }
        return render(request,'articles/upate.html',context)
    
    
@require_POST
def comments_create(request,pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail',article.pk)
    return redirect('accounts:login')

@require_POST
def comments_delete(request,article_pk,comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail',article_pk)
            