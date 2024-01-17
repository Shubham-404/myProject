from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from myApp.models import SellerInfo, customer, Output, product
from myApp.ai_model import aimodel
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
        email=request.POST.get("email")
        # password=request.POST.get("password")    
        info=customer(name=name, mobile=email)
        info.save()
        return redirect('/done')
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
    op=aimodel("https://www.canyon.com/dw/image/v2/BCML_PRD/on/demandware.static/-/Sites-canyon-master/default/dw3b5264c3/images/full/147861_910/2018/147861_9100155_Canyon_Snapback_bk_wh.jpg?sw=750&sfrm=png&q=90&bgcolor=F2F2F2")
    result = op

    # Save the result to the database
    Output.objects.create(result=result)

    # Retrieve all stored results
    all_results = Output.objects.all()

    return render(request, 'AiModel.html', {'result': result, 'all_results': all_results})
