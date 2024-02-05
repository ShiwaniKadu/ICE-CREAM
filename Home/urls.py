from django.contrib import admin
from django.urls import path
from Home.views import *


urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("services/", services, name="services"),
    path("contact/", contact, name="contact"),
    path("icecream/", icecream, name="Icecream"),
]
