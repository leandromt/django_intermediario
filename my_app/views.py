from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from .models import Address, STATE_CHOICE
from .forms import AddressForm


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
    if request.method == 'GET':
        form = AddressForm()
    else:
        form = AddressForm(request.POST)
        if form.is_valid():
            Address.objects.create(
                address=form.cleaned_data['address'],
                address_complement=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                country=form.cleaned_data['country'],
                user=request.user
            )
            return redirect('/addresses/')
        
    return render(request, 'my_app/address/create.html', {'form': form})


@login_required(login_url='/login')
def address_update(request, id):
    address = Address.objects.get(id=id)

    if request.method == 'GET':
        form = AddressForm()
        return render(request, 'my_app/address/update.html', {'form': form})

    address.address = request.POST.get('address')
    address.address_complement = request.POST.get('address_complement')
    address.city = request.POST.get('city')
    address.state = request.POST.get('state')
    address.country = request.POST.get('country')
    # address.user = request.user

    address.save()


    return redirect('/addresses/')
