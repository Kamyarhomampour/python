format_output = "\033[47m\033[30m"
format_reset = "\033[0m"
# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")

import requests
API_key='0d05c675e37e1e7bcd4eb42e9e128118'
print("Welcom to this page.")
City = input("which city are you from?")
print(f"You are from {City}.")
weather_data = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?q={City}&units=imperial&APPID={API_key}")
weather=weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])
wind_speed = (weather_data.json()['wind']['speed'])
print(f"Today's weather is {weather}")
print(f"Today's temperature is{temp} .")
print(f"Today's speed is {wind_speed}")


print(f"{format_output}---END---{format_reset}")