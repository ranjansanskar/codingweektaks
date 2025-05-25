import requests

class WeatherExtractor:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def fetch_weather(self, location):
        params = {
            "q": location,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()

            weather = {
                "location": data.get("name"),
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"]
            }

            return weather

        except requests.RequestException as e:
            return {"error": str(e)}
        except KeyError:
            return {"error": "Unexpected response format."}