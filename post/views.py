from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("cohort13")


def greet(request):
    return HttpResponse("Hi")


def eat(request):
    return HttpResponse("Chop 🍴")


def htmlTag(request):
    return render(request, 'htmlTag.html')
