from django.shortcuts import render, HttpResponse
from myApp.models import SellerInfo, customer

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
        # return HttpResponse("Done bro!!")
    else:
        return render(request, "signin.html")
        # return HttpResponse("This is Signin Page!")
def buyer(request):
    return render(request, "buyer.html")
    # return HttpResponse("This is Buyer's Page!")
def seller(request):
    return render(request, "seller.html")
    # return HttpResponse("This is Seller's Page!")
def contact(request):
    # return render(request, "contact.html")
    return HttpResponse("This is Contact's Page!")

def sellerinfo(request):
    if request.method == "POST":
        name = request.POST.get("sellerName")
        email = request.POST.get("sellerEmail")
        address = request.POST.get("selleraddress")
        phone = request.POST.get("sellerphone")
        info = SellerInfo(sellername=name, selleremail=email, selleraddress=address, sellerphone=phone)
        info.save()
        # return 
    else:
        return render(request, "sellerinfo.html")
    
