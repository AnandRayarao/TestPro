from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def Home(request):
    return HttpResponse("This is home page")

def News(request):
    return HttpResponse("This is news page")

def About(request):
    return HttpResponse("This is about page")