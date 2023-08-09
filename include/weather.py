import requests
import json

api_key_openweather = "693b23e6c8d06c26925c1f8e83dfb011"


def get_current_weather(location, unit="celsius", api_key=api_key_openweather):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    url = (BASE_URL + "?q=" + location + "&units=" + unit + "&appid=" + api_key)

    response = requests.get(url)


    if response.status_code == 200:
        data = response.json()

        temperature_kelvin = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        weather_description = data['weather'][0]['description']

        if unit == "celsius":
            temperature = temperature_kelvin - 273.15
        else:
            temperature = temperature_kelvin * 9 / 5 - 459.67

        weather_info = {
            "location": location,
            "temperature": temperature,
            "unit": unit,
            "humidity": humidity,
            "pressure": pressure,
            "weather_description": weather_description
        }

        return json.dumps(weather_info)
    else:
        return None

def get_forecast_weather(location, unit="celsius", api_key=api_key_openweather):
    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

    url = (BASE_URL + "?q=" + location + "&units=" + unit + "&appid=" + api_key)

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        forecast = data['list']

        forecast_info = []

        for item in forecast:
            forecast_info.append({
                "location": location,
                "temperature": item['main']['temp'],
                "unit": unit,
                "humidity": item['main']['humidity'],
                "pressure": item['main']['pressure'],
                "weather_description": item['weather'][0]['description'],
                "date": item['dt_txt']
            })

        return json.dumps(forecast_info)
    else:
        return None
