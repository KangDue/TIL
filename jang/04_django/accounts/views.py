from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout 
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.
def login(request):
    if request.user.is_authenticated: #사전 차단.
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            #로그인. (=not save) (save = 화원가입)
            # create session
            auth_login(request,form.get_user())#2번째 인자인 유저정보 어디서?
            print("---------------------")
            print(request.GET.get('next'))
            print("-------------------")
            return redirect(request.GET.get('next')or 'articles:index') #단축평가

    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # save함수는 user를 반환함.
            auth_login(request,user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/signup.html',context)

def delete(request):
    auth_logout(request) #
    request.user.delete() #요청 user 정보를 가지고 있음
    return redirect('articles:index')

def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(instance = request.user)
        if form.is_valid():
            form.save()
            redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context={
        'form':form
    }
    return render(request,'accounts/update.html',context)

def pwchange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }
    return render(request,'accounts/pwchange.html',context)