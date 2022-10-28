from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from .serializers import *
from rest_framework.decorators import api_view
# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


# @login_required
@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user: 
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


@api_view(['POST'])
def comments_create(request, pk):
    if request.user.is_authenticated:
        print(request.data)
        article = get_object_or_404(Article, pk=pk)
        cs = CommentSerializer(data=request.data) #값은 data로 받는다.
        if cs.is_valid(raise_exception=True):
            cs.save(article=article, user=request.user)
            return JsonResponse(cs.data)
    return redirect('accounts:login')


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)

@api_view(['POST'])
def comments_update(request,article_pk,comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk = comment_pk)
        if request.user == comment.user:
            print('-------------------------------',request.data)
            cs = CommentSerializer(instance = comment, data = request.data)
            if cs.is_valid(raise_exception=True):
                cs.save()
                return JsonResponse(cs.data)
    return redirect('articles:detail', article_pk)

            


@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
            liked = False
        else:
            article.like_users.add(request.user)
            liked = True
        context = {
            'liked': liked,
            'count': article.like_users.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:login')
