import os
from io import BytesIO

import requests
from dotenv import load_dotenv
from PIL import Image, ImageTk

load_dotenv()



def get_current_weather(q:str):
    url = f"{os.getenv('BASE_URL')}/current.json?key={os.getenv('API_KEY')}&q={q}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'current' in data and 'condition' in data['current']:
            return {
                'condition': data['current']['condition']['text'],
                'temperature': data['current']['temp_c'],
                'temp_feels_like': data['current']['feelslike_c'],
                'humidity': data['current']['humidity'],
                'icon': data['current']['condition']['icon'],
            }
        else:
            raise Exception("Data wasn't found")
    else:
        raise Exception("Error requesting api", response.status_code)

def get_icon(icon_url:str):
    response = requests.get(icon_url)
    if response.status_code == 200:
        img_data = Image.open(BytesIO(response.content))
        return img_data


def get_forecast_weather(q: str):
    url = f"{os.getenv('BASE_URL')}/forecast.json?key={os.getenv('API_KEY')}&q={q}&days=3&aqi=no&alerts=no&hour=12"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'current' in data and 'condition' in data['current']:
            current_data = {
                'condition': data['current']['condition']['text'],
                'temperature': data['current']['temp_c'],
                'temp_feels_like': data['current']['feelslike_c'],
                'humidity': data['current']['humidity'],
                'icon': data['current']['condition']['icon'],
            }
            forecast_data = []

            for forecast_day in data['forecast']['forecastday']:
                forecast_data.append({
                    'date': forecast_day['date'],
                    'condition': forecast_day['day']['condition']['text'],
                    'max_temperature': forecast_day['day']['maxtemp_c'],
                    'min_temperature': forecast_day['day']['mintemp_c'],
                    'icon': forecast_day['day']['condition']['icon'],
                })

            return {
                'current': current_data,
                'forecast': forecast_data
            }
        else:
            raise Exception("Data wasn't found")
    else:
        raise Exception("Error requesting api", response.status_code)
