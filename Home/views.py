from django.shortcuts import render,redirect
from datetime import datetime
from .models import *
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def index(request):
    messages.success(request,"This is a test messages")
    return render(request, "index.html")
    
   
def about(request):
    #return HttpResponse("This is about page")
    return render(request, "about.html")

def services(request):
    #return HttpResponse("This is services page")
    return render(request, "services.html")

def contact(request):
    #return HttpResponse("This is contact page")
    if request.method =="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,"Your message has been sent!")
       

    return render(request, "contact.html")

def icecream(request):
    if request.method == "POST":

        data = request.POST
        icecream_image = request.FILES.get("IceCream_image")
        icecream_name = data.get("IceCream_name")
        icecream_description = data.get("IceCream_description")
        print(icecream_image)
        print(icecream_name)
        print(icecream_description)
        IceCream.objects.create(
            icecream_image=icecream_image,
            icecream_name=icecream_name,
            icecream_description=icecream_description,
        )
        return redirect("/icecream/")
    queryset = IceCream.objects.all()
    if request.GET.get("search"):
        queryset = queryset.filter(icecream_name__icontains = request.GET.get("search"))
    context = {"icecreams" : queryset}
    return render(request, "icecream.html",context)

def delete_icecream(request, id):

    queryset = IceCream.objects.get(id=id)
    queryset.delete()
    return redirect("/icecream/")

def update_icecream(request, id):
    queryset = IceCream.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        icecream_image=request.FILES.get("icecream_name")
        icecream_name = data.get("IceCream_name")
        icecream_description = data.get("IceCream_description")

        queryset.icecream_name = icecream_name
        queryset.icecream_description = icecream_description

        if icecream_image:
            queryset.icecream_image = icecream_image

        queryset.save()  
        return redirect("/icecream/")  

    context = {"icecream" : queryset}

    return render(request ,"update_icecream.html",context)