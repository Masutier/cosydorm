from django.contrib import messages
from django.shortcuts import render, redirect


def home (request):

    context={"title": "Home"}
    return render(request, 'cosydorm/home.html', context)


def laundry(request):

    context={"title": "Laundry"}
    return render(request, 'cosydorm/laundry.html', context)
