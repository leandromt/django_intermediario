from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout


def login(request):

    if request.method == 'GET':
        return render(request, 'my_app/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
        #return HttpResponse('Usuário válido!!')
        django_login(request, user)
        #return HttpResponseRedirect('/home/')
        return redirect('/home/')
    else:
        message = 'Usuário ou senha inválidos!'
        return render(request, 'my_app/login.html', {'message': message})


def home(request):
    return render(request, 'my_app/home.html')


def logout(request):
    django_logout(request)
    return redirect('/login/')
