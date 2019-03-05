from django.shortcuts import render
import requests
from django.shortcuts import render,redirect
from .models import City
from .forms import CityForm
from django.views.decorators.http import require_POST

def indexx(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&APPID=365a9cdd0b5c3311e3232c7e9c6c4a9b'
    form=CityForm()
    weather_data=[]
    cities=City.objects.all()
    for city in cities:
        r=requests.get(url.format(city.name)).json()
        city_weather={
          'city':city,
          'temperature':r['main']['temp'],
          'description':r['weather'][0]['description'],
          'icon':r['weather'][0]['icon']
          }

        weather_data.append(city_weather)
    context= {'weather_data':weather_data,'form':form}
    return render(request,"weather/index1.html",context)
@require_POST
def addCity(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&APPID=365a9cdd0b5c3311e3232c7e9c6c4a9b'
    form=CityForm(request.POST)
    if(form.is_valid()):
        form.save()
    return redirect('/')
