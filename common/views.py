from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from common.forms import UserForm
from django.http import JsonResponse


def mypage(request):

    return render(request, 'common/mypage.html')


# 회원 가입
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # username=form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request,user) 저절로 로그인 시켜줌
            return redirect('common:login')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def id_check(request):
    try:
        user=User.objects.get(username=request.GET['username'])
        #몾찾으면 에러

    except:
        user = None
    res = {
        'data' : 'good' if user else 'not good'
    }
    return JsonResponse(res)




