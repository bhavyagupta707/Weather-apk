import requests
import json
import pyttsx3

city = input("Enter a name of city:")
url = f"https://api.weatherapi.com/v1/current.json?key=f0df3acc5f6e46f587785328262606&q={city}"


r = requests.get(url)
print(r.text)
print(type(r.text))

wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
s = wdic["current"]["wind_kph"]
h = wdic["current"]["humidity"]

pyttsx3.speak(f"The current temperature in {city} is {w} degrees")
pyttsx3.speak(f"The current wind speed in {city} is {s} kph")
pyttsx3.speak(f"The current humidity in {city} is {h} ")
