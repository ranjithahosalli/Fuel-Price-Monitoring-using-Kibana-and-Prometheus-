import pytest
from models.fuel_price import FuelPrice
from services.data_fetcher import DataFetcher

def test_average_price():
    fetcher = DataFetcher()
    prices = fetcher.get_prices()
    avg = sum(fp.price for fp in prices) / len(prices)
    assert isinstance(avg, float)
    assert 60 <= avg <= 120

def test_percentage_change():
    fetcher = DataFetcher()
    prices_before = [fp.price for fp in fetcher.get_prices()]
    fetcher.update_prices()
    prices_after = [fp.price for fp in fetcher.get_prices()]
    changes = [(after - before) / before * 100 for after, before in zip(prices_after, prices_before)]
    for change in changes:
        assert -1 <= change <= 1  # Within allowed simulated bounds
