from django.shortcuts import render
import dialogflow
# Create your views here.
def complaint(request):
    return render(request,"complaint.html",{})
