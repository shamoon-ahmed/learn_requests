import requests
import os

API_KEY = os.getenv("WEATHER_API_KEY")

# fetching a user profile so we just pass the url with the user id and get response
r = requests.get("https://www.linkedin.com/in/shamoon-ahmed-496a6231b/")

print("Response: ", r.text)
print("Status Code: ", r.status_code)

# fetching the weather, we pass some parameters. Those parameters are are visible in the url
# the requests library automatically encodes the query like %20 or + in place of a space ( )

city = input("Enter City: ").capitalize()

params = {
    "q" : city,
    "appid" : API_KEY
}

url = f"http://api.openweathermap.org/geo/1.0/direct"

r = requests.get(url, params=params)
data = r.json()
lat = data[0]["lat"]
lon = data[0]["lon"]
print("Response -> ", "City: ", data[0]["name"], "| Country: ", data[0]["country"], "| Latitude: ", data[0]["lat"], "| Longitude: ", data[0]["lon"])

parameters = {
    "lat" : lat,
    "lon" : lon,
    "appid" : API_KEY
}

weather_url = "https://api.openweathermap.org/data/2.5/weather"

r = requests.get(weather_url, params=parameters)

weather_data = r.json()

print("Response -> ", "City: ", data[0]["name"], "| Country: ", data[0]["country"], "| Weather: ", weather_data["weather"][0]["main"], "| Description: ", weather_data["weather"][0]["description"])

