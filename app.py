import os
from flask import Flask, jsonify
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
from services.data_fetcher import DataFetcher
from services.metrics_exporter import MetricsExporter
from services.elastic_logger import ElasticLogger
from config.settings import FETCH_INTERVAL

# Load env vars
load_dotenv()

app = Flask(__name__)
fetcher = DataFetcher()
metrics_exporter = MetricsExporter()
elastic_logger = ElasticLogger()

@app.route('/')
def health():
    return jsonify({'status': 'ok', 'details': 'Fuel Price Monitoring API running.'})

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


def periodic_update_job():
    # Simulate price updates
    fetcher.update_prices()
    new_prices = fetcher.get_prices()
    metrics_exporter.update_metrics(new_prices)
    elastic_logger.log_price_updates(new_prices)

# Scheduler setup
sched = BackgroundScheduler(daemon=True)
sched.add_job(periodic_update_job, 'interval', seconds=FETCH_INTERVAL)
sched.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

