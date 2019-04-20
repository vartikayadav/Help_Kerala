from django.shortcuts import render,redirect
from .models import Hospital
from . import forms
from .models import Patient
# Create your views here.
def medical1(request):
    data=Hospital.objects.all()
    # if request.method=="POST":
    #     form=forms.PatientForm(request.POST)
    #     obj=Patient.objects.create(
    #     name=request.POST['name'],
    #     age=request.POST['age'],
    #     phoneno=request.POST['phoneno'],
    #     problem=request.POST['problem'],
    #
    #     )
    #     if form.is_valid():
    #         form.save()
    #     return redirect("/")
    form=forms.PatientForm()
    return render(request,"medicalcare/medicalcare.html",{'data':data,'form':form})
