from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_safe,require_http_methods,require_POST

# @require_http_method(['method1','method2']) 는 허용 접근방식 지정가능
# @require_post 단순히 post 필터링 뿐만 아니라 적절한 응답까지 줌.

# Create your views here.
@require_safe # get만 허용함
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


#new와 create의 method만 구분되면 둘이 합칠수 있지 않니?
#new를 create에 녹여보자

# def new(request): #새 페이지 내놔 get 요청만 받음
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)

def create(request): # new의 post만 받음.
    if request.method == 'POST':
    #create
        form = ArticleForm(request.POST)
        if form.is_valid(): #is_valid를 통과하지 못했을때.. else 바깥으로 빠짐
            article = form.save()
            return redirect('articles:detail', article.pk)
        # print(f'에러: {form.errors}')
    else:
    #new
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)





    # 사용자의 데이터를 받아서
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    # article = Article(title=title, content=content)
    # article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/index.html')
    # return redirect('/articles/')
    # return redirect('articles:index')
    # return redirect('articles:detail', article.pk)


def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

#push delete patch등 다양한 method가 존재
#따라서 get말고 post를 먼저 확인한다.
#DB 입장에서 우선순위 조정
#나중에 u = put, d = delete로 method 교체함.
def delete(request, pk): # get에대한 처리를 할 필요가 없다.
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('articles:index')

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        # form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else: # 논리구조상 else부터 작성해야함. 기본페이지 우선
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)






    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)
