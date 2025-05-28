from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def chai(request):
    return render(request, 'chai/chai_temp.html')

def order(request):
    return HttpResponse("Hello there how are you")