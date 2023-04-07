from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ContUs
from .forms import ContactForm, reviewForm


@login_required(login_url='loginPage')
def raiting(request):
    user = request.user
    if request.method == 'POST':
        form = reviewForm(request.POST)

        if form.is_valid():
            pform = form.save(commit=False)
            pform.user  = user
            pform.message  = request.POST.get('message')
            pform.stars  = request.POST.get('stars')
            pform.save()

            messages.success(request, f"Your review was created successfully")
            return redirect("home")
        else:
            messages.error(request, f"Something went wrong. We are sorry")
            return redirect("home")
    else:
        form = reviewForm()

    context={"title":"Testing", "banner":"Review Testing", "form":form}
    return render(request, 'raiting/raiting.html', context)


def us(request):
    contactMess = ContUs.objects.all()
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactUs = form.save()
            messages.success(request, f"Something went wrong. We are sorry")
            return redirect("home")
        else:
            messages.error(request, f"Something went wrong. We are sorry")
            return redirect("home")

    context={"title": "US", "banner": "Contact Us", "form": form, "contactMess":contactMess}
    return render(request, 'raiting/contactUs.html', context)


@login_required(login_url='loginPage')
def testing(request):
    if request.method == 'POST':
        form = reviewForm(request.POST)

        if form.is_valid():
            pform = form.save(commit=False)
            pform.user  = request.user
            pform.save()
            messages.success(request, f"Your review was created successfully")
            return redirect("home")
        else:
            messages.error(request, f"Something went wrong. We are sorry")
            return redirect("home")
    else:
        form = reviewForm()

    context={"title":"Testing", "banner":"Review Testing", "form":form}
    return render(request, 'raiting/test.html', context)


# mailing
