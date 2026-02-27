# Fuel-Price-Monitoring-using-Kibana-and-Prometheus-
# Real-Time Fuel Price Monitoring System

## Overview
This microservice tracks real-time fuel prices across Indian cities or states, simulates market updates OR fetches live data (from configured API), and exposes Prometheus-compatible metrics. It logs price events to Elasticsearch for visualization in Kibana. Useful for analytics, transparency, and anomaly detection.

## Tech Stack
- Python 3.10+ (Flask, APScheduler, prometheus_client)
- Elasticsearch 8.x, Kibana 8.x
- Prometheus (metrics & alerting)
- Docker & Docker Compose

## Folder Structure
```
fuel-monitoring/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── prometheus.yml
├── prometheus.rules.yml
├── .env.example
├── README.md
│
├── models/
├── services/
├── config/
├── tests/
└── mock_api/
    ├── mock_api.py
    └── Dockerfile
```

## Setup Instructions
### 1. Build & Run Everything (Docker Compose)
```bash
docker-compose up --build
```
### 2. Manual Setup (For development)
- Install Python 3.10+
- Create/activate virtualenv
- Install requirements: `pip install -r requirements.txt`
- Fill `.env` from `.env.example`
- Start dependencies (Elasticsearch, Prometheus, Kibana)
- Run Flask app: `python app.py`

### 3. Access Endpoints
- Flask app: [http://localhost:5000](http://localhost:5000)
- Prometheus: [http://localhost:9090](http://localhost:9090)
- Kibana: [http://localhost:5601](http://localhost:5601)
- Elasticsearch: [http://localhost:9200](http://localhost:9200)
- Mock API: [http://localhost:8000/v1/prices](http://localhost:8000/v1/prices)

### 4. Test Prometheus Metrics
```bash
curl http://localhost:5000/metrics
```

### 5. Kibana Dashboard Setup
- In Kibana, add index pattern: `fuel-price-events*`
- Visualize: Average fuel price by city, by time
- Add alert for spikes (see Prometheus alert)

## API Endpoints
- `/` — Health check
- `/metrics` — Prometheus metrics

## Prometheus Alerts
Trigger: `fuel_price > 130` for 1 minute (see prometheus.rules.yml).

## Using the Mock Live Fuel Price API (No API Key Needed)
- A mock API is included as a service (`mockapi`) that returns:
```json
{
  "prices": [
    {"city": "mum", "fuel_type": "Petrol", "price": 105.4},
    {"city": "mum", "fuel_type": "Diesel", "price": 95.1},
    ...
  ]
}
```
- To enable live fetching from the mock API, set:
  - `USE_LIVE_API=1`
  - `API_URL=http://mockapi:8000/v1/prices` (already set via docker-compose for the app service)
  - `API_KEY` is optional for the mock and ignored.

Example `.env` variables:
```
ELASTIC_URL=http://elasticsearch:9200
ELASTIC_INDEX=fuel-price-events
API_KEY=
FETCH_INTERVAL=15
USE_LIVE_API=1
API_URL=http://mockapi:8000/v1/prices
```

### Try It
- Start stack: `docker-compose up --build`
- Confirm mock API: `curl http://localhost:8000/v1/prices`
- Confirm app metrics reflect mock updates after a few seconds: `curl http://localhost:5000/metrics | rg fuel_price`

## Example Test Commands
```bash
pytest tests/
curl http://localhost:5000/metrics
curl http://localhost:5000
```

## Screenshots
*Optional: Add images showing metrics in Prometheus & dashboards in Kibana*

