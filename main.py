import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()


twilio_sid = os.getenv('TWILIO_ACCOUNT_SID')
twilio_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
weather_api_key = os.getenv('WEATHER_API_KEY')
zone = 'bogota'
days = '1'
url = f'http://api.weatherapi.com/v1/forecast.json?key={weather_api_key}&q={zone}&days={days}&aqi=no&alerts=no'


response = requests.get(url).json()