from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods,require_POST,require_safe
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

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
    context = {
        'form':form
    }
    return render(request,'articles/create.html',context)


@require_safe
def detail(request,pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comments.all()
    context = {
        'article':article,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request,'articles/detail.html',context)

@require_POST
def delete(request,pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated and request.user == article.user:
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail',article.pk)


@login_required
@require_http_methods(['GET','POST'])
def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(data=request.POST,instance = article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail',pk)
    else:
        form = ArticleForm(instance=Article)
    context = {
        'form':form,
        'article':article,
    }
    return render(request,'articles/update.html',context)

@require_POST
def comment_create(request,article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.articles = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail',article.pk)
    return redirect('accounts:login') #그냥 로그인 req 달면 안되남 ?


@require_POST
def comment_delete(request,article_pk,comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk = comment_pk)
        if request.user == comment.user:
            comment.delete()
            return redirect('articles:index', article_pk)

@require_POST
def likes(request,article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')