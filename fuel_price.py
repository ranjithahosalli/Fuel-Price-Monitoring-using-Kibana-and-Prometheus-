from datetime import datetime

class FuelPrice:
    def __init__(self, city, fuel_type, price, timestamp=None):
        self.city = city
        self.fuel_type = fuel_type
        self.price = price
        self.timestamp = timestamp or datetime.utcnow()

    def __repr__(self):
        return f'<FuelPrice city={self.city} fuel_type={self.fuel_type} price={self.price} timestamp={self.timestamp}>'

