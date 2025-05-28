from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("This is my first django and this is Home page")
    return render(request, 'Websites\index.html')


def about(request):
    return HttpResponse("This is my first django and this is About page")


def contact(request):
    return HttpResponse("This is my first django and this is Contact page")