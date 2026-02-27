from services.metrics_exporter import MetricsExporter
from models.fuel_price import FuelPrice


def test_metrics_exporter_updates():
    metrics = MetricsExporter()
    prices = [
        FuelPrice('mum', 'Petrol', 110),
        FuelPrice('dlh', 'Diesel', 95)
    ]
    # Call to update metrics
    metrics.update_metrics(prices)
    # The Gauge values should match inserted prices
    assert metrics.price_gauge.labels(city='mum', fuel_type='Petrol')._value.get() == 110
    assert metrics.price_gauge.labels(city='dlh', fuel_type='Diesel')._value.get() == 95
    # Counter increments: test one more update
    before = metrics.update_counter.labels(city='mum')._value.get()
    metrics.update_metrics([FuelPrice('mum', 'Petrol', 112)])
    after = metrics.update_counter.labels(city='mum')._value.get()
    assert after == before + 1
