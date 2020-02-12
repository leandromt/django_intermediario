from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from .models import Address


def login(request: HttpRequest):

    if request.method == 'GET':
        return render(request, 'my_app/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
        print(user)
        #return HttpResponse('Usuário válido!!')
        django_login(request, user)
        #return HttpResponseRedirect('/home/')
        return redirect('/home/')

    message = 'Usuário ou senha inválidos!'
    return render(request, 'my_app/login.html', {'message': message})


@login_required(login_url='/login')
def logout(request):
    django_logout(request)
    return redirect('/login/')


@login_required(login_url='/login')
def home(request):
    return render(request, 'my_app/home.html')


@login_required(login_url='/login')
def address_list(request):
    # addresses = Address.objects.all()
    addresses = Address.objects.all().filter().order_by('address')
    return render(request, 'my_app/address/list.html', {'addresses': addresses})


@login_required(login_url='/login')
def address_create(request):
    addresses = Address.objects.all().filter().order_by('address')
    return render(request, 'my_app/address/create.html', {'addresses': addresses})
