from django.shortcuts import render

# Django 회원가입 구현 지원
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'border/border.html')
        else:
            return render(request, 'registration/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'registration/login.html')

def logout(request):
    pass

def register(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user( # user 생성
                username=request.POST["username"],password=request.POST["password1"])
            auth.login(request,user)
            return render(request, "login.html")
        return render(request, 'register.html')


    return render(request, 'registration/register.html') # accounts/register 접속 시 해당 줄 실행

