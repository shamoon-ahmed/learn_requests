import requests
import os

# # EXAMPLE 1:

# # fetching a user profile so we just pass the url with the user id and get response
# r = requests.get("https://www.linkedin.com/in/shamoon-ahmed-496a6231b/")

# print("Response: ", r.text)
# print("Status Code: ", r.status_code)

# # EXAMPLE 2:

# # fetching the weather, we pass some parameters. Those parameters are are visible in the url
# # the requests library automatically encodes the query like %20 or + in place of a space ( )
# # not every url gives a json response. instead they give html text response

# API_KEY = os.getenv("WEATHER_API_KEY")

# city = input("Enter City: ").capitalize()

# params = {
#     "q" : city,
#     "appid" : API_KEY
# }

# url = f"http://api.openweathermap.org/geo/1.0/direct"

# r = requests.get(url, params=params)
# data = r.json()
# lat = data[0]["lat"]
# lon = data[0]["lon"]
# print("Response -> ", "City: ", data[0]["name"], "| Country: ", data[0]["country"], "| Latitude: ", data[0]["lat"], "| Longitude: ", data[0]["lon"])

# parameters = {
#     "lat" : lat,
#     "lon" : lon,
#     "appid" : API_KEY
# }

# weather_url = "https://api.openweathermap.org/data/2.5/weather"

# r = requests.get(weather_url, params=parameters)

# weather_data = r.json()

# print("Response -> ", "City: ", data[0]["name"], "| Country: ", data[0]["country"], "| Weather: ", weather_data["weather"][0]["main"], "| Description: ", weather_data["weather"][0]["description"])

# EXAMPLE 3: 
url = "https://media.greatbigphotographyworld.com/wp-content/uploads/2014/11/Landscape-Photography-steps.jpg"
image = requests.get(url)

with open("Landscape-Photography-steps.jpg", "wb") as f:
    f.write(image.content)
