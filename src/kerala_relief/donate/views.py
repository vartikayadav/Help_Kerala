from django.shortcuts import render,redirect
from . import forms
import stripe
from django.conf import settings
from .models import Donate
from django.contrib import messages
#create your views here

def donate(request):
    stripe.api_key=settings.STRIPE_SECRET_KEY
    data_key=settings.STRIPE_PUBLISHABLE_KEY
    description="Help_Kerala"
    total=int(10000)
    if request.method=="POST":

        try:
            form=forms.UserDonateForm(request.POST)
            total=int(request.POST['amount'])*100
            token=request.POST['stripeToken']
            email=request.POST['stripeEmail']
            customer=stripe.Customer.create(
            email=email,
            source=token
            )
            charge=stripe.Charge.create(
            amount=total,
            currency="INR",
            description=description,
            customer=customer.id
            )
            obj=Donate.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            amount=request.POST['amount'],

            )
            obj.save()
            if form.is_valid():
                form.save()

        except stripe.error.CardError as e:
            return e
        messages.add_message(request, messages.SUCCESS, 'Thanks for donation....')    
        return redirect("/")

    else:
        if request.user.is_authenticated:
            form=forms.UserDonateForm()
            context={"form":form,'stripe.api_key':stripe.api_key,'data_key':data_key,'description':description}
            return render(request,"donate/donate.html",context)
        else:
            messages.add_message(request, messages.SUCCESS, 'You need to login to donate....')

            return redirect("/")
