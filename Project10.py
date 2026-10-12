import requests
import os
def get_weather_data(city):
    api_key = "81c6c77c82bb9e1920c0de66fc06bd38"  # Replace with your actual API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "humidity": "true",
        "pressure": "true",
        "wind": "true"
    }
    response = requests.get(base_url, params=params)
    return response.json()
def display_weather_info(weather_data):
    if weather_data.get("cod") != 200:
        print("Error:", weather_data.get("message"))
        return

    city = weather_data["name"]
    country = weather_data["sys"]["country"]
    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    humidity = weather_data["main"]["humidity"]
    pressure = weather_data["main"]["pressure"]
    wind_speed = weather_data["wind"]["speed"]
    print("=" * 40)
    print("Weather Information".center(40))
    print("=" * 40)
    print(f"{"City":<15}: {city}")
    print(f"{"Country":<15}: {country}")
    print(f"{"Temperature":<15}: {temperature:.2f}°C")
    print(f"{"Description":<15}: {description.capitalize()}")
    print(f"{"Humidity":<15}: {humidity}%")
    print(f"{"Pressure":<15}: {pressure} hPa")
    print(f"{"Wind Speed":<15}: {wind_speed} m/s")
def main():
    try:
        city = input("Enter city name: ")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return
    weather_data = get_weather_data(city)
    display_weather_info(weather_data)
    try:
        search_another = input("Search for another city? (y/n): ").lower()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return
    if search_another == "y" or search_another == "yes":
        main()
    else:
        print("Thank you for using the Weather App!")
if __name__ == "__main__":
    main()