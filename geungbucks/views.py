from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Basket


# 홈 (index)
def home (req):
    return render(req, 'home.html')

# 상세정보 
def about (req):
    return render(req, 'about.html')

# 신상품 소개 
def new_item (req):
    return render(req, 'new_item.html')

# 로그인 
def login (req):
    return render(req, 'common/login.html')

# 계정 생성 
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            auth_login(request, user)  # 로그인
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})