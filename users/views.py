from django.shortcuts import render, redirect
from .forms import ConnexionForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from datetime import datetime
from supper.models import Participation, Day

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = ConnexionForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if not user:
            error = "Mauvais nom d'utilisateur ou mot de passe" 
        else:
            auth_login(request, user)
            return redirect('index')

    return render(request, 'users/login.html', locals())

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.first_name = form.cleaned_data['firstname']
        user.last_name = form.cleaned_data['lastname']
        user.email = form.cleaned_data['mail']
        user.internal = form.cleaned_data['internal']
        user.kot = form.cleaned_data['kot']
        kot = form.cleaned_data['kot']
        if kot.password == form.cleaned_data['kotPassword']:
            user.save()
            if user.internal:
                days = Day.objects.filter(date__gt=datetime.today())
                for day in days:
                    Participation.objects.create(user=user, day=day)
            user = authenticate(request, username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'])
            auth_login(request, user)
            return redirect('index')


    return render(request, 'users/register.html', locals())

@login_required
def logout(request):
    auth_logout(request)
    return redirect('users:login')