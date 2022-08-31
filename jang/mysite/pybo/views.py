from django.shortcuts import render

# Create your views here.
from .models import Question

def index(request):
  question_list = Question.objects.order_by('-create_date')
  context  = {'question':question_list}
  return render(request,'pybo/question_list.html',context)