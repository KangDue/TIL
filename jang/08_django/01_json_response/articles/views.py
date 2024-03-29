from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import ArticleSerializer
from .models import Article
from django.http.response import JsonResponse,HttpResponse
from django.core import serializers


# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []
    for article in articles:
        articles_json.append(
            {
                'id':article.pk,
                'title':article.title,
                'content':article.content,
                'created_at':article.created_at,
                'updated_at':article.updated_at,
            }
        )
    return JsonResponse(articles_json,safe=False) #인자 자체가 dict 가 아니면 safe=False해줘야함


def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json',articles)
    return HttpResponse(data,content_type='application/json')


# @api_view(['GET'])
@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
