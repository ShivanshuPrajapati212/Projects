from bs4 import BeautifulSoup
import requests
import os
import json


# Weather Status
key = os.environ['KEY']

query = input("Enter a search query: ")

url = f"https://api.weatherapi.com/v1/current.json?key={os.environ['KEY']}&q={query}&aqi=no"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
data = json.loads(soup.text)

print("Location :", data["location"]["name"])
print("Time :", data["location"]["localtime"])
print("Temperature in Celsius:", data["current"]["temp_c"])
print("Temperature in Fahrenheit :", data["current"]["temp_f"])
print("Wind Speed :", data["current"]["wind_kph"])
print("Humidity :", data["current"]["humidity"])
