from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def about(request):
    return HttpResponse("<h1>welcome to about page</h1>")
def donate(request):
    return HttpResponse("<h1>welcome to donate page</h1>")
