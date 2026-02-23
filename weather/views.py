from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

# Replace with your OpenWeather API key
API_KEY = '621e4a07473ad0d26f566bace492fdd3'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@csrf_exempt
def get_weather(request):
    city = request.GET.get('city', None)  # Get city from form submission

    if not city:
        # Render the template without weather data if no city is provided
        return render(request, 'weather/weather.html')

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Get temperature in Celsius
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Format the response data
        formatted_data = {
            'city': data.get('name'),
            'temperature': f"{data['main']['temp']}°C",
            'feels_like': f"{data['main']['feels_like']}°C",
            'weather': data['weather'][0]['description'].capitalize(),
            'humidity': f"{data['main']['humidity']}%",
            'wind_speed': f"{data['wind']['speed']} m/s",
            'sunrise': datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%I:%M %p'),
            'sunset': datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%I:%M %p'),
            'is_cold': data['main']['temp'] < 15
        }

        # Render the HTML template with the formatted data
        return render(request, 'weather/weather.html', formatted_data)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': 'Failed to fetch weather data', 'details': str(e)}, status=500)
