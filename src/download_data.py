import requests
import pandas as pd

url = "https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude": 33.6844,
    "longitude": 73.0479,
    "start_date": "2015-01-01",
    "end_date": "2025-12-31",

    "daily": ",".join([
        "temperature_2m_mean",
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
        "rain_sum",
        "wind_speed_10m_max",
    ]),

    "timezone": "Asia/Karachi",
    "temperature_unit": "celsius",
    "wind_speed_unit": "kmh",
    "precipitation_unit": "mm",
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.url)
data = response.json()

df = pd.DataFrame(data["daily"])

print(df.head())
print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nInformation:")
print(df.info())

print("\nStatistics:")
print(df.describe())
df.to_csv(
    "data/islamabad_weather_2015_2025.csv",
    index=False
)

print("\nDataset saved successfully!")
print(df.head())