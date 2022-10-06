from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from articles.forms import ArticleForm, CommentForm
from .models import Article,Comment
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context={'articles':articles}
    return render(request,'articles/index.html',context)

@login_required
def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                article= form.save(commit=False)
                article.user = request.user
                article.save()
                return redirect('articles:detail',article.pk)
        else:
            form = ArticleForm()
        context = {
            'form':form
        }
        return render(request, 'articles/create.html',context)

@login_required
@require_POST
def delete(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    print(request.method)
    article.delete()
    return redirect('articles:index')

def detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()#html 상에서 직접 불러도 됨.

    context = {
        'article':article,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request,'articles/detail.html',context)

def comment_create(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment=form.save(commit=False)
        comment.article=article
        comment.save()
    return redirect('articles:detail',article_pk)

@login_required
@require_POST
def comment_delete(request,article_pk,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail',article_pk)