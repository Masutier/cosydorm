from django.contrib import messages
from django.shortcuts import render, redirect
from .models import ContUs
from .forms import ContactForm


def home (request):

    context={"title": "Home", "banner": "Home"}
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


def testimonials(request):
    contMess = ContUs.objects.all()
    form = ContactForm()

    context={"title": "Testimonials", "banner": "Testimonials", 'contMess':contMess, "form": form}
    return render(request, 'cosydorm/testimonials.html', context)


def fq(request):

    context={"title": "F & Q", "banner": "Frequently Asked Questions"}
    return render(request, 'cosydorm/fq.html', context)


def us(request):
    contactMess = ContUs.objects.all()
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactUs = form.save()
            messages.success(request, f"Message created and sended")
            return redirect("home")
        else:
            messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return redirect("home")

    context={"title": "US", "banner": "Contact Us", "form": form, "contactMess":contactMess}
    return render(request, 'cosydorm/contactUs.html', context)

