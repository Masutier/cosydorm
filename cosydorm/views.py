from django.contrib import messages
from django.shortcuts import render, redirect
from raiting.models import ReviewUs


def home (request):
    reviews = ReviewUs.objects.all()

    context={"title": "Home", "banner": "Home", 'reviews':reviews}
    return render(request, 'cosydorm/home.html', context)


def laundry(request):

    context={"title": "Laundry", "banner": "Laundry"}
    return render(request, 'cosydorm/laundry.html', context)


def dryClean(request):

    context={"title": "Dry Cleaning", "banner": "dryClean"}
    return render(request, 'cosydorm/dryClean.html', context)


def cleaning(request):

    context={"title": "Cleaning", "banner": "Cleaning"}
    return render(request, 'cosydorm/cleaning.html', context)


def storage(request):

    context={"title": "Storage", "banner": "Storage"}
    return render(request, 'cosydorm/storage.html', context)


def fq(request):

    context={"title": "F & Q", "banner": "Frequently Asked Questions"}
    return render(request, 'cosydorm/fq.html', context)
