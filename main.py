import requests
import os
from datetime import datetime

user_api = '5a3829162baa2f3c6656589b44c425a1'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print("invalid city: {}, Please check your name".format(location))
else:
    temp_city = ((api_data['main']['temp'])-273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("--------------------------------------------------")
    print("Weather Stats for - {} || {}".format(location.upper(), date_time))

    print("--------------------------------------------------")
    print("Current temperature is: {:.2f} deg C".format(temp_city))
    print("Current weather description: ",weather_desc)
    print("Curren6t Humidity : ",hmdt,'%')
    print("Current wind speed :",wind_spd,'kmph')