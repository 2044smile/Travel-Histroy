from django.shortcuts import render
from .forms import LoginForm, registerForm
# Django 회원가입 구현 지원
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from border import models

def login(request):
    br = models.Border.objects.all()
    context = {'title':br}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'border/border.html',context)
        else:
            return render(request, 'registration/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'registration/login.html')

def logout(request):
    pass

def register(request):
    if request.method == 'POST':
        register_form = registerForm(request.POST)
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # 유효성 검증에 통과한 경우(username의 중복과 password1,2 의 일치 여부)
        if register_form.is_valid():
            # registerForm의 인스턴스 메서드인 register() 실행, 유저생성
            register_form.signup()
            return render(request, 'registration/login.html')
        elif password1 != password2:
            return render(request, 'registration/register.html', {'error': 'Confirm your password entry.'})
        else:
            return render(request, 'registration/register.html', {'error': 'An ID that already exists.'})
    else:
        register_form = registerForm()


    context = {
        'register_form': register_form,
    }
    return render(request, 'registration/register.html', context)

