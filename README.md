
## Weather App

This is a command-line weather app that grabs live data from OpenWeatherMap. You can check the current temperature, humidity, pressure, wind speed, and get a quick weather description for pretty much any city on the planet.

## What It Does

- You type in a city name.
- It pulls actual weather data from OpenWeatherMap.
- Shows you temperature, humidity, pressure, wind speed—basically all the main stuff.
- Output looks organized and easy to read.
- If something goes wrong (wrong city, API issues), it lets you know and won’t crash.
- You can search for as many cities as you want without restarting (thanks to recursion).
- Handles keyboard interrupts like Ctrl+C without freaking out.

## Features

- Full weather report: temp, humidity, pressure, wind speed, description.
- Real-time: uses the requests library to fetch live data.
- Solid error messages: lets you know if the city isn’t found or if the API fails.
- Clean output: info lines up in a neat table—not messy.
- Search as many cities as you want without restarting.
- Catches KeyboardInterrupt, so you can shut it down without ugly errors.
- Parses JSON to pull data out of nested responses.
- Recursion lets you keep searching cities without loops.

## How to Run

Step 1: Install the requests library
```bash
pip install requests
```
Step 2: Get API Key
- There’s an API key in the code already.
- Want your own? Sign up at https://openweathermap.org/api, grab your key.

Step 3: Run It
```bash
python weather_app.py
```
## Example Output
```python
Enter city name: London
========================================
        Weather Information
========================================
City           : London
Country        : GB
Temperature    : 27.31°C
Description    : Overcast clouds
Humidity       : 52%
Pressure       : 1016 hPa
Wind Speed     : 4.12 m/s
Search for another city? (y/n): y
Enter city name: Tokyo
========================================
        Weather Information
========================================
City           : Tokyo
Country        : JP
Temperature    : 24.44°C
Description    : Overcast clouds
Humidity       : 84%
Pressure       : 1013 hPa
Wind Speed     : 4.12 m/s
Search for another city? (y/n): n
Thank you for using the Weather App!
```
## What I Learned

- Sending HTTP requests with Python requests.
- Figuring out how API endpoints, base URLs, and parameters work.
- Parsing JSON to dig out what I actually want.
- Checking response codes to catch errors.
- Lining up text output with f-strings and nice formatting.
- Graceful shutdown for user input—no ugly KeyboardInterrupt.
- Recursion to keep searching without loops.
- Passing parameters like city name, API key, units through the API.
- Digging into deep-nested dictionaries for real-world data.
- Connecting a Python app to live internet data—feels pretty satisfying.

## Code Structure
```python
def get_weather_data(city):
    # Builds the API request, sends it, returns JSON data.

def display_weather_info(weather_data):
    # Checks if API call worked, pulls out weather info, and prints it nicely.

def main():
    # Takes city input, fetches weather, shows output.
    # Keeps asking if you want to search again, uses recursion.
    # Handles KeyboardInterrupt for a clean exit.
```
## API Response Structure

city name → weather_data["name"]
country → weather_data["sys"]["country"]
temperature → weather_data["main"]["temp"]
description → weather_data["weather"][0]["description"]
humidity → weather_data["main"]["humidity"]
pressure → weather_data["main"]["pressure"]
wind_speed → weather_data["wind"]["speed"]

## Challenges

- Nested dictionaries: digging out weather[0]["description"] is actually awkward.
- Getting f-string formatting just right so columns line up.
- Handling API errors: catching when cod != 200 and showing a nice message.
- KeyboardInterrupt: letting users quit without staring at a traceback.
- Using recursion instead of a loop to repeat searches.
- Case sensitivity: turns out “Tokyo”, “tyoko”, or “TOKYO” all work fine.
- API key security: I realized hardcoding a key is risky if you share code publicly.

## What Works

✓ Handles typos—if you type “Tyoko”, it tells you “city not found” and lets you try again.
✓ Lets you search a bunch of cities back-to-back, no restarts.
✓ Output is clean and easy to read.
✓ Error messages are clear—no confusion when something goes wrong.
✓ Friendly—thanks messages and gentle exits.

## Things I Could Add

- Save favorite cities in a file.
- Display weather forecast (next five days).
- Show sunrise and sunset times.
- Let you pick units: Celsius, Fahrenheit, Kelvin.
- Store API key in environment variables—much safer.
- Search by coordinates.
- Show weather icons.
- Compare weather across cities.
- Add weather alerts.
- Local cache for cities (don't hammer API needlessly).

## Why This Matters

This project proves I can:
- Use real APIs and work with live internet data.
- Handle errors and actually tell the user what happened.
- Write code that's organized—one function, one job.
- Make output look professional, not messy.
- Keep the app running smoothly with recursion.
- Handle user input calmly (no crashing).

## Some key takeaways:
- Real apps rely on APIs.
- APIs send you JSON, which is just Python dictionaries most of the time.
- Error handling isn’t optional—things fail.
- User experience counts: formatting, messages, exits.
- Apps shouldn’t live in their own bubble—they connect to the real world.

This isn’t “just practicing.” It’s building something useful that talks to real servers.

---

## Important Notes

Security Notice:
- The API key is hardcoded right now (not ideal for public repos).
- You should use environment variables in real projects:
```python
import os
api_key = os.getenv("OPENWEATHER_API_KEY")
```
Set it up like this:
```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```
That’s safer in the long run, but the current version works for learning.

## Requirements:
- Python 3.6+
- requests library (pip install requests)
- Internet connection
- API key (already in code)

---

## Real Output vs Expected

Test Case 1: Valid city (London)
✓ Shows weather correctly, asks if you want to search again, handles “y”

Test Case 2: Typo (Tyoko)
✓ Tells you “city not found,” lets you retry, gets weather for “Tokyo” after correction

Test Case 3: Exit
✓ Handles “n” gracefully, thanks the user, exits cleanly

All handled perfectly.

---

## Next Steps

For next time:
- Move API key to environment variables.
- Add caching so it doesn’t keep calling API for the same city.
- Add a forecast.
- Maybe turn it into a web app using Flask.
- Deploy it somewhere so anyone can use it.

As it stands, this app is pretty robust for a learning project. Real apps are actually built this way!

Next up: more features and improvements 🌍

