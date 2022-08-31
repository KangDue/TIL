from django.shortcuts import render

# Create your views here.
def index(request):
  context  = {'like':['딸기','바나나','파인애플','복숭아','망고']
  ,'hate':['딸기','복숭아']
  }
  return render(request,'fruits/index.html',context)