from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Article,Comment
from .serializers import ArticleListSerializer, ArticleSerializer,CommentSerializer
from django.shortcuts import get_object_or_404,get_list_or_404
# 주소 끝에 / 필수
# decorator 필수
@api_view(['GET','POST']) #httep 4가지 method list로 입력, 기본값은 get
def article_list(request):
    if request.method == 'GET': #대소문자 구분 해야함...
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True): #400띄우기 효과
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  #생성 성공 201
        #return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST) #실패는 400 오류 떠야함.
    
        
        
#다른 method는 405 not allowed 뜸.

#기존 조회시 댓글목록은 안보임
# 1. 기존필드 오버라이드 | 필드 추가
@api_view(['GET','DELETE','PUT']) # http에선 대소문자 구분 없는데, python은 구분
def article_datail(request,article_pk):
    article = get_object_or_404(Article,pk = article_pk)

    if request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = ArticleSerializer(instance = article, data = request.data) #instance가 앞에 들어감
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data)



@api_view(['GET','POST']) #httep 4가지 method list로 입력, 기본값은 get
def comment_list(request):
    if request.method == 'GET': #대소문자 구분 해야함...
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True): #400띄우기 효과
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  #생성 성공 201
        #return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST) #실패는 400 오류 떠야함.
    
@api_view(['GET','DELETE','PUT']) # http에선 대소문자 구분 없는데, python은 구분
def comment_detail(request,comment_pk):
    comment = get_object_or_404(Comment,pk = comment_pk)
    
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = CommentSerializer(instance = comment, data = request.data) #instance가 앞에 들어감
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data)

#400 badrequest article field is required 뜸.
#그냥 보내면 article 정보때문에 오류가뜸. 읽기 전용 필드로 바꿔줘야함.
@api_view(['GET','POST']) #각 방법에 맞게 변환해줌. 안하면 forbidden 뜬다. 403
def comment_create(request,article_pk):
    article = get_object_or_404(Article,pk = article_pk)
    serializer = CommentSerializer(data = request.POST)
    if serializer.is_valid(raise_exception = True): #400띄우기 효과
        serializer.save(article = article) #commit 대신 이렇게 넣어주면 됨.
        return Response(serializer.data, status=status.HTTP_201_CREATED)  #생성 성공 201