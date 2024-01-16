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
    path("contact", views.contact, name="contact"),
    path("sellerinfo", views.sellerinfo, name="sellerinfo"),
]
