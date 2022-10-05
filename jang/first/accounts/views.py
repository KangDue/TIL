from django.shortcuts import render,redirect
from .forms import CustomUserChangeForm, CustomUserCreationFrom
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_safe,require_POST
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated: # 이미 로그인한 사용자 접근시 되돌림
        return redirect('articles:index')
    
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect(request.GET.get('next') or 'articles:index') #next로 날려져온 페이지로 감.
    else:
        form = AuthenticationForm()
    context ={
        'form':form,
    }
    return render(request,'accounts/login.html',context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request) #로그아웃은 로그인 상태일때만, 하면됨. 
    return redirect('articles:index')

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationFrom(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user) #유저 정보만 있으면 바로 로그인 가능!
            return redirect('articles:index')
    else:
        form = CustomUserCreationFrom()
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html',context)

@require_POST
def delete(request): #request.user로 직접 객체 가져오기 가능
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)#탈퇴후 로그아웃 해줌.
    return redirect('articles:index')

@require_http_methods(['GET', 'POST'])
@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form
    }
    return render(request,'accounts/update.html',context)

@require_http_methods(['GET', 'POST'])
@login_required
def pwchange(request):
    if request.method=="POST":
        form = PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context={
        'form':form
    }
    return render(request,'accounts/pwchange.html',context)
