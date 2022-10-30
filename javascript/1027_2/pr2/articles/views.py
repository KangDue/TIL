import re
from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods,require_POST,require_safe
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.shortcuts import get_list_or_404,get_object_or_404
# Create your views here.
def index(request):
    articles = Article.objects.all()#get_list_or_404(Article)
    context = {
        'articles':articles
    }
    return render(request,'articles/index.html',context)


@require_http_methods(['GET','POST'])
def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ArticleForm(data=request.POST)
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
    return redirect('articles:index')


@require_safe
def detail(request,pk):
    article = get_object_or_404(Article,pk=pk)
    comments = article.comment_set.all()
    form = CommentForm()
    context = {
        'article':article,
        'form':form,
        'comments':comments
    }
    return render(request,'articles/detail.html',context)

@require_http_methods(['GET','POST'])
def update(request,pk):
    article = get_object_or_404(Article,pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            form = ArticleForm(instance=article,data=request.POST)
            if form.is_valid():
                article = form.save()
                article.save()
                return redirect('articles:detail',article.pk)
        else:
            form = ArticleForm(instance=article)
            context = {
                'form':form
            }
            return render(request,'articles/create.html',context)
    return redirect('articles:index')

@require_POST
def delete(request,pk):
    article = get_object_or_404(Article,pk=pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')

@require_POST
def comment_create(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    form = CommentForm(data = request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save() #저장을 해줘야 db에 저장됨.
    return redirect('articles:detail',article_pk)

@require_http_methods(['GET','POST'])
def comment_update(request,article_pk,comment_pk):
    article = get_object_or_404(Article,pk=article_pk)
    comment = get_object_or_404(Comment,pk=comment_pk)
    if request.method == "POST":
        form = CommentForm(instance = comment,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = CommentForm(instance=comment)
        context = {
            'form':form,
            'comment':comment
        }
        return render(request,'articles/comment_update.html',context)
    
@require_POST
def comment_delete(request,article_pk,comment_pk):
    article = get_object_or_404(Article,pk=article_pk)
    comment = get_object_or_404(Comment,pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail',article.pk)

@require_POST
def likes(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if request.user.is_authenticated:
        if request.user != article.user:
            if article.like_users.filter(pk=request.user.pk).exists():
                article.like_users.remove(request.user)
            else:
                article.like_users.add(request.user)
    print(request.POST)
    if request.POST.get('index'):
        return redirect('articles:index')
    else:
        return redirect('articles:detail',article_pk)