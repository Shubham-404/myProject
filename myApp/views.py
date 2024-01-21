from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from myApp.models import SellerInfo, customer, Output, product
from myApp.ai_model import aimodel
from django.contrib import messages
# messages.error
# messages.success
# messages.debug
# messages.info
# messages.warning

from random import randint

# Create your views here.
def about(request):
    return render(request, "about.html")
    # return HttpResponse("This is HomePage!")
def home(request):
    return render(request, "home.html")
    # return HttpResponse("This is HomePage!")
def signin(request):
    if request.method=="POST":
        name=request.POST.get("fname")+" "+request.POST.get("lname")
        mobile=request.POST.get("mobile")
        # password=request.POST.get("password")
        info=customer(name=name, mobile=mobile)
        info.save()
        messages.success(request, f"Hurray! You were Registered Successfully! Kindly LogIn.✔")
        return redirect('/signin')
        # return HttpResponse("Done bro!!")    
    return render(request, "signin.html")
        # return HttpResponse("This is Signin Page!")
def buyer(request):
    return render(request, "buyer.html")
    # return HttpResponse("This is Buyer's Page!")
def seller(request):
    return render(request, "seller.html")

def contact(request):
    # return render(request, "contact.html")
    return HttpResponse("This is Contact's Page!")
def done(request):
    return render(request, "done.html")

def ask(request):
    return render(request, "ask.html")
def shirts(request):
    return render(request, "shirts.html")
def pants(request):
    return render(request, "pants.html")
def caps(request):
    return render(request, "caps.html")

def sellproduct(request):
    if request.method=="POST":
        id=randint(100000, 999999)
        price=request.POST.get("productPrice")
        category=request.POST.get("productName")
        stock=request.POST.get("stock")
        img=request.POST.get("productImg")
        # password=request.POST.get("password")    
        info=product(productid=id, price=price, category=category, img=img, stock=stock)
        info.save() 
        return redirect('/AiModel')
    return render(request, "sellproduct.html")
    # return HttpResponse("This is sellproduct's Page!")

def sellerinfo(request):
    if request.method == "POST":
        name = request.POST.get("sellerName")
        email = request.POST.get("sellerEmail")
        address = request.POST.get("selleraddress")
        phone = request.POST.get("sellerphone")
        info = SellerInfo(sellername=name, selleremail=email, selleraddress=address, sellerphone=phone)
        info.save()
        return redirect('/sellproduct')
        # return 
    
    return render(request, "sellerinfo.html")
    

def AiModel(request):
    op=aimodel("https://i5.walmartimages.com/asr/38e07a08-f83e-4459-a37b-514ae22a60b2.341925d96639ba229923fcb9b8a5b40e.jpeg?odnHeight=768&odnWidth=768&odnBg=FFFFFF")
    result = op

    # Save the result to the database
    Output.objects.create(result=result)

    # Retrieve all stored results
    all_results = Output.objects.all()

    return render(request, 'AiModel.html', {'result': result, 'all_results': all_results})
