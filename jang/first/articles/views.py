from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request,'articles/index.html',context)

@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method =='POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request,'articles/create.html',context)


@require_safe
def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request,'articles/detail.html',context)

@require_POST
def delete(request,pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

@login_required
@require_http_methods(['GET','POST'])
def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm(instance = article)
    context = {
        'form':form,
        'article':article,
    }
    return render(request,'articles/update.html',context)



#-------------------------기타 과제 ----------------
def greeting(request):
    foods = ['apple','banana','coconut']
    info = {'name':'Alice'}
    context = {
        'foods':foods,
        'info':info,
    }
    return render(request,'articles/greeting.html',{'name':'Alice'})

def dinner(request):
    foods = ['족발','햄버거','치킨','초밥']
    context = {
        'foods':foods,
    }
    return render(request,'articles/dinner.html',context)

def throw(request):
    return render(request,'articles/throw.html')

def catch(request):
    message = request.GET.get('num1')
    context = {
        'num':message,
    }
    return render(request,'articles/catch.html',context)