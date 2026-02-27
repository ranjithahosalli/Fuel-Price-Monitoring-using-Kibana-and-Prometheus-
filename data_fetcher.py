import os
import random
from datetime import datetime
from models.fuel_price import FuelPrice
from models.city import City
import requests

class DataFetcher:
    def __init__(self):
        self.cities = [
            City('mum', 'Mumbai', 'Maharashtra'),
            City('dlh', 'Delhi', 'Delhi'),
            City('chn', 'Chennai', 'Tamil Nadu'),
            City('bng', 'Bangalore', 'Karnataka'),
        ]
        self.fuel_types = ['Petrol', 'Diesel']
        self.prices = {(city.slug, ft): FuelPrice(city.slug, ft, 100 + random.uniform(0, 10)) for city in self.cities for ft in self.fuel_types}
        self.use_live_api = os.getenv('USE_LIVE_API', '0') == '1'
        self.api_key = os.getenv('API_KEY', None)
        self.api_url = os.getenv('API_URL', 'http://mockapi:8000/v1/prices')

    def fetch_from_api(self):
        """Fetch data from configured API. API key is optional for mock usage."""
        try:
            params = {
                "cities": ','.join([city.slug for city in self.cities])
            }
            if self.api_key:
                params["apikey"] = self.api_key
            resp = requests.get(self.api_url, params=params, timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                for rec in data.get('prices', []):
                    key = (rec['city'], rec['fuel_type'])
                    if key in self.prices:
                        self.prices[key].price = rec['price']
                        self.prices[key].timestamp = datetime.utcnow()
                return True
        except Exception as e:
            print(f"[DataFetcher] fetch_from_api failed: {e}")
        return False

    def update_prices(self):
        if self.use_live_api and self.fetch_from_api():
            return self.prices
        # fallback: simulate
        for key, fp in self.prices.items():
            variation = random.uniform(-0.5, 0.5)
            fp.price = max(60, fp.price + variation)
            fp.timestamp = datetime.utcnow()
        return self.prices

    def get_prices(self):
        return list(self.prices.values())

