from prometheus_client import Gauge, Counter

class MetricsExporter:
    def __init__(self):
        self.price_gauge = Gauge('fuel_price', 'Current fuel price', ['city', 'fuel_type'])
        self.update_counter = Counter('price_updates_total', 'Number of price updates', ['city'])

    def update_metrics(self, fuel_prices):
        for fp in fuel_prices:
            self.price_gauge.labels(city=fp.city, fuel_type=fp.fuel_type).set(fp.price)
            self.update_counter.labels(city=fp.city).inc()

