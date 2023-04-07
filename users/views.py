import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import *


@unauthenticated_user
def registerUser(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            group = Group.objects.get(name='user_rol')
            user.groups.add(group)
            login(request, user)
            messages.success(request, f'The User was created successfuly, Now create the rest of the info')
            return redirect("registerProfile")
        else:
            messages.error(request, f"Something went wrong. We are sorry")
            return redirect("home")
    else:
        form = UserRegisterForm()

    context = {'title':'User Register', "banner": "User Register", 'form':form}
    return render(request, 'users/registerUser.html', context)


@login_required(login_url='loginPage')
def registerProfile(request):
    cities = []
    userAuth = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            prof_form = form.save(commit=False)
            prof_form.user = userAuth
            prof_form.save()
            messages.success(request, f'The account was created successfuly')
            return redirect('home')
        else:
            messages.error(request, f"Something went wrong. We are sorry")
            return redirect("home")
    else:
        form = ProfileForm()

        with open('static/json/us_states_and_cities.json') as statesFile:
            states = json.load(statesFile)

            for j in states['Florida']:
                cities.append(j)
            cities.sort()

    context = {'title':'Register Profile', "banner": "Register Profile", 'form':form, 'cities':cities}
    return render(request, 'users/registerProfile.html', context)


@unauthenticated_user
def loginPage(request):
    form = LogInForm()
    
    if request.method == 'POST':
        form = LogInForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, f'Algo no salio bien, Intentalo de nuevo')
            return redirect('home')

    context = {'title':'LogIn', 'form':form}
    return render(request, 'users/login.html', context)



def userLogout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='loginPage')
def userProfile(request):
    user_profile = request.user.profile

    context = {'title':'User Profile', 'banner':"Profile", 'user_profile':user_profile}
    return render(request, 'users/user_profile.html', context)


@login_required(login_url='loginPage')
def editProfile(request):
    cities = []
    user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            pform = form.save(commit=False)
            pform.user  = request.POST.get('user')
            pform.phone  = request.POST.get('phone')
            pform.institute = request.POST.get('institute')
            pform.address1 = request.POST.get('address1')
            pform.address2 = request.POST.get('address2')
            pform.state = request.POST.get('state')
            pform.zip = request.POST.get('zip')

            pform.save()

            messages.success(request, f'Modifications was saved successfuly')
            return redirect('userProfile')
        else:

            messages.error(request, f"Something went wrong. We are sorry")
            return redirect("home")
    else:
        form = ProfileForm()

        with open('static/json/us_states_and_cities.json') as statesFile:
            states = json.load(statesFile)

            for j in states['Florida']:
                cities.append(j)
            cities.sort()

    context = {'title':'Register Profile', "banner": "Register Profile", 'form':form, 'profile':profile, 'cities':cities}
    return render(request, 'users/edit_profile.html', context)
