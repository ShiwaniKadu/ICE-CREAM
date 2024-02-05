from django.shortcuts import render, redirect
from datetime import datetime
from Home.models import *
from django.contrib import messages


# Create your views here.
def index(request):
    messages.success(request, "This is a test messages")
    return render(request, "index.html")


def about(request):
    # return HttpResponse("This is about page")
    return render(request, "about.html")


def services(request):
    # return HttpResponse("This is services page")
    return render(request, "services.html")


def contact(request):
    # return HttpResponse("This is contact page")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(
            name=name, email=email, phone=phone, desc=desc, date=datetime.today()
        )
        contact.save()
        messages.success(request, "Your message has been sent!")

    return render(request, "contact.html")


def icecream(request):
    if request.method == "POST":

        data = request.POST
        IceCream_image = request.FILES.get("IceCream_image")
        IceCream_name = data.get("IceCream_name")
        IceCream_description = data.get("IceCream_description")

        IceCream.objects.create(
            IceCream_image=IceCream_image,
            IceCream_name=IceCream_name,
            IceCream_description=IceCream_description,
        )
        return redirect("/")

    queryset = IceCream.objects.all()

    if request.GET.get("search"):
        queryset = queryset.filter(IceCream_name__icontains=request.GET.get("search"))
    context = {"icecream": queryset}

    return render(request, "icecream.html", context)
