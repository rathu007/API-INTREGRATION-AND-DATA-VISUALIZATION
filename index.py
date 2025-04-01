import requests 
import matplotlib.pyplot as plt
import seaborn as sns

# OpenWeatherMap API details
API_KEY = "6ba6e2bb7ac88635bf5fe92c2ea3a70a"  # Replace with your new API key
CITY = "london"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data
response = requests.get(URL)
data = response.json()

# Check if the response contains the expected data
if 'list' not in data:
    print("Error fetching data:", data)  # Print the error message
else:
    # Extract relevant data
    dates = [entry['dt_txt'] for entry in data['list']]
    temperatures = [entry['main']['temp'] for entry in data['list']]
    humidity = [entry['main']['humidity'] for entry in data['list']]

    # Visualization
    plt.figure(figsize=(12, 6))
    sns.set_style("darkgrid")

    # Temperature plot
    plt.plot(dates, temperatures, marker="o", label="Temperature (°C)", color="tab:red")
    plt.xticks(rotation=45)

    # Humidity plot
    plt.plot(dates, humidity, marker="s", label="Humidity (%)", color="tab:blue")

    plt.xlabel("Date & Time")
    plt.ylabel("Values")
    plt.title(f"Weather Forecast for {CITY}")
    plt.legend()
    plt.show()

