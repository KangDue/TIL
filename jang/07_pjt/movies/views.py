import re
from django.shortcuts import render,get_list_or_404,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
@api_view(['GET'])
def actor_list(request):
    actors = get_list_or_404(Actor)
    data = ActorListSerializer(actors,many=True)
    return Response(data.data)

@api_view(['GET'])
def actor_detail(request,actor_pk):
    actor = get_object_or_404(Actor,pk=actor_pk)
    data = ActorSerializer(actor)
    return Response(data.data)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    data = MovieListSerializer(movies,many=True)
    return Response(data.data)

@api_view(['GET'])
def movie_detail(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    data = MovieSerializer(movie)
    return Response(data.data)

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    data = ReviewListSerializer(reviews,many=True)
    return Response(data.data)

@api_view(['GET','PUT','DELETE'])
def review_detail(request,review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        data = ReviewSerializer(review)
        return Response(data.data)
    if request.method == 'PUT':
        data = ReviewSerializer(instance=review,data=request.data)
        if data.is_valid(raise_exception=True):
            data.save()
            return Response(data.data)
    if request.method == 'DELETE':
        review.delete()
        info = {"delete":f"review {review_pk} is deleted"}
        return Response(info,status=204)
    
@api_view(['POST'])
def create_review(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    data = ReviewSerializer(data=request.data)
    if data.is_valid(raise_exception=True):
        data.save(movie=movie)
        return Response(data.data,status=201)