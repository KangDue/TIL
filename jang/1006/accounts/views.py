from django.shortcuts import render,redirect
from .form import CustomUserCreationForm,CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST,require_http_methods,require_safe
"""
인증 - request 필요,
단순 db - request.post만 있으면 됨.
업데이트 - instance 필요
"""
# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            auth_login(request,form.save())
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html',context)

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('articles:index')

# @require_http_methods(['POST','GET'])
def login(request):
    if request.method=="POST":
        print(1232152142131,request)
        # request와 request.post 둘 다 필요.
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            print(request.GET, '?'*30)
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context={
        'form':form,
    }
    return render(request,'accounts/login.html',context)
##########################
# @login_required
# @require_POST
# def delete(request,article_pk):
#     article = Article.objects.get(pk=article_pk)
#     article.delete()
#     return redirect('articles:index')


# def login(request):
#     if request.user.is_authenticated:
#         return redirect('articles:index')
#     if request.method=="POST":
#         form = AuthenticationForm(request,request.POST)
#         if form.is_valid():
#             auth_login(request,form.get_user())
#             return redirect(request.GET.get('next') or 'articles:index')
#     else:
#         form = AuthenticationForm()
#     context={
#         'form':form,
#     }
#     return render(request,'accounts/login.html',context)