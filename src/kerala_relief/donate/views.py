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
    total=int(100)
    if request.method=="POST":
        #print(request.POST)#stripe module generates the token
        try:
            form=forms.UserDonateForm(request.POST)
            token=request.POST['stripeToken']
            email=request.POST['stripeEmail']
            customer=stripe.Customer.create(
            email=email,
            source=token
            )
            charge=stripe.Charge.create(
            amount=total,
            currency="gbp",
            description=description,
            customer=customer.id
            )


            if form.is_valid():
                form.save()
        except stripe.error.CardError as e:
            return e
        return redirect("/")

    else:
        if request.user.is_authenticated:
            form=forms.UserDonateForm()
            context={"form":form,'stripe.api_key':stripe.api_key,'data_key':data_key,'description':description,'total':total}
            return render(request,"donate/donate.html",context)
        else:
            messages.add_message(request, messages.SUCCESS, 'You need to login to donate....')

            return redirect("/")
