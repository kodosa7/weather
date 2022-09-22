from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import City
from datetime import datetime, time
import requests

# Create your views here.

# homepage view with list of cities and links to them
def home_view(request):
    queryset = City.objects.all()
    context = { 'cities': queryset }
    return render(request, 'home_view.html', context)

# single city view by id
def city_id_view(request, id):
    city = get_object_or_404(City, id=id)

    # takes API_KEY from settings.py
    api_key = settings.API_KEY
    api_address = "http://api.openweathermap.org/data/2.5/weather?q=" + str(city) + "&appid=" + api_key

    json_data = requests.get(api_address).json()
    kelvin = json_data["main"]["temp"]
    celsius = round(kelvin - 273.15, 2)

    for item in json_data['weather']:
        get_weather_type = item['main']

    for item in json_data['weather']:
        get_weather_desc = item['description']

    currentTemp = celsius
    weatherType = get_weather_type
    weatherDesc = get_weather_desc
    windSpeed = json_data["wind"]["speed"]
    currentTime = datetime.now()

    # chooses a number for the weather condition background picture
    # and checks if time is day or night
    if weatherType == "Rain":
        if time(7, 0) <= currentTime.time() <= time(19, 0):
            bgPic = 1
        else:
            bgPic = 5
    if weatherType == "Snow":
        if time(7, 0) <= currentTime.time() <= time(19, 0):
            bgPic = 2
        else:
            bgPic = 6
    if weatherType == "Clear":
        if time(7, 0) <= currentTime.time() <= time(19, 0):
            bgPic = 3
        else:
            bgPic = 7
    if weatherType == "Clouds":
        if time(7, 0) <= currentTime.time() <= time(19, 0):
            bgPic = 4
        else:
            bgPic = 8

    context = { 'thisCity': city,
                'thisTemp': currentTemp,
                'thisWeatherType': weatherType,
                'thisWeatherDesc': weatherDesc,
                'thisWindSpeed': windSpeed,
                'thisCurrentTime': currentTime,
                'thisBgPic': bgPic }
    
    return render(request, 'city.html', context)
