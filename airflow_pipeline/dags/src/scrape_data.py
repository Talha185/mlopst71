import requests
import pandas as pd
from datetime import datetime

API_KEY = "b5344551e91ab1ceb68f3be846b3a99d"
CITY = "Lahore"

BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&APPID={API_KEY}"

def fetcher():

    
    response = requests.get(BASE_URL)
    data = response.json()

    data = {
        "Temp": data["main"]["temp"],
        "Humid": data["main"]["humidity"],
        "Wind Sp": data["wind"]["speed"],
        "Weather Cond": data["weather"][0]["description"],
    }

    df = pd.DataFrame([data])
    df.to_csv("D:\\mlopst7\\datasets\\data.csv", index=False, header=False)

if __name__ == "__main__":
    fetcher()
