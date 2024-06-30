

# Import necessary libraries
import requests  # For making HTTP requests to the OpenWeatherMap API
import os  # For interacting with the operating system, particularly for environment variables
from dotenv import load_dotenv  # For loading environment variables from a .env file
from bs4 import BeautifulSoup  # For parsing HTML (Note: This import is not used in the current script)
import csv  # For reading and writing CSV files
from datetime import datetime  # For adding timestamps to our weather data


# Load environment variables from .env file
# This is crucial for keeping sensitive information like API keys secure
load_dotenv()

def get_weather(city):
    """
    Fetch weather data for a given city using the OpenWeatherMap API.
    
    Key aspects:
    - API key: Stored in an environment variable for security
    - API endpoint: Constructed using f-string with city name and API key
    - Error handling: Uses try-except to manage potential API request issues
    """
    # Retrieve API key from environment variables
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Ensure OPENWEATHERMAP_API_KEY is set in your .env file.")
    
    # Construct the API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        # Send GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the JSON response
        data = response.json()
        
        # Extract relevant weather information
        # This creates a dictionary with specific weather details
        weather_data = {
            'city': city,
            'temperature': f"{data['main']['temp']}°C",
            'condition': data['weather'][0]['description'],
            'humidity': f"{data['main']['humidity']}%"
        }
        return weather_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response content: {response.content}")  # Print response content for debugging
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    return None

def save_to_csv(data, filename):
    """
    Save the collected weather data to a CSV file.
    
    Key aspects:
    - CSV structure: Defines the fields for the CSV file
    - Timestamp: Adds a timestamp to each weather data entry
    - File handling: Uses 'with' statement for proper file handling
    """
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['city', 'temperature', 'condition', 'humidity', 'timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for item in data:
            item['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow(item)
    
    print(f"Data saved to {filename}")

def main():
    """
    Main function to orchestrate the weather data collection and saving process.
    
    Key steps:
    1. Define a list of cities
    2. Get user input for an additional country
    3. Fetch weather data for all cities (including user input)
    4. Save collected data to a CSV file
    """
    # List of predefined cities
    cities = ['New York', 'London', 'Tokyo', 'Sydney', 'Moscow']
    all_weather_data = []  # List to store weather data for all cities
    
    # Fetch weather data for each city
    for city in cities:
        print(f"Fetching weather data for {city}...")
        weather_data = get_weather(city)
        if weather_data:
            all_weather_data.append(weather_data)
    
    # Save the collected weather data to a CSV file
    if all_weather_data:
        save_to_csv(all_weather_data, 'Weather data/weather_data.csv')
    else:
        print("No data to save.")

# Entry point of the script
if __name__ == "__main__":
    main()

"""
Overall Codebase Explanation:

1. Environment Setup:
   - The script uses a .env file to store the API key securely.
   - The load_dotenv() function loads this key into the environment.

2. API Interaction (get_weather function):
   - Constructs a URL for the OpenWeatherMap API using the city name and API key.
   - Sends a GET request to this URL.
   - Parses the JSON response to extract relevant weather information.
   - Implements error handling for potential API request issues.

3. Data Processing:
   - Weather data for each city is stored in a dictionary format.
   - These dictionaries are collected in the all_weather_data list.

4. User Interaction:
   - The script allows users to add a country of their choice to the predefined list.

5. Data Persistence (save_to_csv function):
   - Collected weather data is saved to a CSV file.
   - Each entry in the CSV includes a timestamp of when the data was collected.

6. Main Execution Flow:
   - Starts with a predefined list of cities.
   - Adds user input to this list.
   - Iterates through the cities, fetching weather data for each.
   - Saves the collected data to a CSV file.

Key Variables:
- api_key: Stores the OpenWeatherMap API key (sensitive information).
- cities: List of cities to fetch weather data for.
- all_weather_data: List that stores weather data dictionaries for all cities.
- weather_data: Dictionary containing weather information for a single city.

This script demonstrates key programming concepts including API interaction, 
file I/O, error handling, and basic user interaction, all centered around 
the task of collecting and storing weather data.
"""