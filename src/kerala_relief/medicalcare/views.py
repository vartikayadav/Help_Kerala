from django.shortcuts import render
from .models import Hospital
# Create your views here.
def medical1(request):
    data=Hospital.objects.all()
    return render(request,"medicalcare/medicalcare.html",{'data':data})
