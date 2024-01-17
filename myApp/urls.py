from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path("", views.home, name="myApp"),
    path("home", views.home, name="home"),
    path("signin/", views.signin, name="signin"),
    path("buyer", views.buyer, name="buyer"),
    path("seller", views.seller, name="seller"),
    path("about", views.about, name="about"),
    path("sellerinfo", views.sellerinfo, name="sellerinfo"),
    path("contact", views.contact, name="contact"),
    path("done", views.done, name="done"),
    path("ask", views.ask, name="ask"),
    path("shirts", views.shirts, name="shirts"),
    path("pants", views.pants, name="pants"),
    path("caps", views.caps, name="caps"),
    path("sellproduct", views.sellproduct, name="sellproduct"),
    path("AiModel", views.AiModel, name="AiModel"),

]

