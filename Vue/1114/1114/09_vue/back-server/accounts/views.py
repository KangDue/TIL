from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
# Create your views here.
class SignupView(APIView):
    def post(self,request):
        user = models.User.objects.create(username=request.data['username'],
        password=request.data['password'],email=request.data['email'])
        user.save()
        token = Token.objects.create(user=user)
        print(token.key)
        return Response({"Token":token.key})
