from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import authenticate
from account.models import User,Bookmark
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from cat_inf.models import Cat
import json

def main(request):
    cats = Cat.objects.all()
    count = Cat.objects.count()
    content = {
        "cats":cats,
        "count":count
    }
    return render(request,'account/main.html',content)

def bookmark(request):
    if(request.method == 'POST'):
        is_marked = request.POST['is_marked']

        if(is_marked == 'true'):
            post = Bookmark()
            post.cat_id = request.POST['cat_id']
            post.user_id = request.user
            post.save()
            print("suc2")
        else:
            id = int(request.POST['cat_id'])
            Bookmark.objects.filter(cat_id = id).delete()
            print("suc1")
            print(type(id))
    return render(request,'cat_inf/create.html') 


def mypage(request):
    pass

def login(request):
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            messages.error(request,'사용자 ID 또는 비밀번호가 일치하지 않습니다.')
            return render(request, 'account/login.html')
        '''
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
        return redirect('main')
        #return render(request,'account/login.html')
        '''
    else:
        form = AuthenticationForm()
        return render(request,'account/login.html', {'form':form})

def logout(request):
    auth_logout(request)
    return redirect('main')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            name=request.POST['name'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'account/signup.html')
    return render(request, 'account/signup.html')

def details(request, cat_id):
    cat_detail = get_object_or_404(Cat, pk=cat_id)
    return render(request, 'details.html',{'cat_detail':cat_detail})