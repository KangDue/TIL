from ast import Pass
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import *
from django.views.decorators.http import require_POST,require_http_methods,require_safe
from django.contrib.auth import get_user_model
# Create your views here.

@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated: # 이미 로그인 상태
        return  redirect('articles:index') 
    else:
        if request.method == "POST":
            form = AuthenticationForm(request,request.POST)
            if form.is_valid(): #form.is_valid()를 안하면 로그인 불가능함.
                auth_login(request,form.get_user())
                return redirect('articles:index')
        else:
            form = AuthenticationForm(request)
        context = {
            'form':form
        }
        return render(request,'accounts/login.html',context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('articles:index')
    
@require_http_methods(['GET','POST'])
def signup(request):
    if request.method == 'POST':
        print(request)
        form = CustomUserCreationForm(data = request.POST)
        if form.is_valid():
            auth_login(request,form.save())
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/signup.html',context)


@require_http_methods(['GET','POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(instance=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form
    }
    return render(request,'accounts/update.html',context)

@require_http_methods(['GET','POST'])
def password_change(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            update_session_auth_hash(request,form.save())
            return redirect('articles:index')
        else:
            form = PasswordChangeForm(request.user)
            context = {
                'form':form,
                'content':'규칙에 맞게 비밀번호를 변경해주세요.'
            }
            return render(request,'accounts/password_change.html',context)
    else:
        form = PasswordChangeForm(request.user)
        context = {
            'form':form
        }
        return render(request,'accounts/password_change.html',context)
    
@require_safe
def profile(request,username):
    person = get_user_model().objects.get(username=username)
    context = {
        'person':person
    }
    return render(request,'accounts/profile.html',context)

@require_POST
def follow(request,username):
    person = get_user_model().objects.get(username=username)
    if request.user.is_authenticated:
        if request.user.pk != person.pk:
            if person.followers.filter(username=request.user).exists():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
    return redirect('accounts:profile', username)
        
    