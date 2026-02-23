# Weather App

## Overview
The Weather App is a Django-based web application that provides weather information for various locations. Users can input a city name to retrieve the current weather conditions for that location.

<img width="1448" height="840" alt="Screenshot 2026-02-23 175141" src="https://github.com/user-attachments/assets/5781ecb2-6063-4af4-937c-dc0f10d54129" />


## Features
- Search for current weather by city name.
- Display weather details such as temperature, humidity, and weather conditions.
- User-friendly interface with a responsive design.

## Key Files
- **manage.py**: Entry point for the Django project.
- **weather/**: Contains the main application code, including models, views, and templates.
- **weather/templates/weather/weather.html**: HTML template for displaying weather information.
- **weather_project/settings.py**: Configuration settings for the Django project.

## Prerequisites
- Python 3.13 or higher
- Django framework

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/weather-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd weather-app
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Run migrations:
   ```bash
   python manage.py migrate
   ```
7. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
1. Open your web browser and navigate to `http://127.0.0.1:8000/`.
2. Enter the name of a city to get the current weather information.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## Acknowledgments
- [Django Documentation](https://docs.djangoproject.com/)
- [OpenWeatherMap API](https://openweathermap.org/api) for providing weather data.
