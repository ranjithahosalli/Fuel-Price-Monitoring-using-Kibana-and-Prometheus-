import os
from dotenv import load_dotenv

load_dotenv()

ELASTIC_URL = os.getenv('ELASTIC_URL', 'http://localhost:9200')
ELASTIC_INDEX = os.getenv('ELASTIC_INDEX', 'fuel-price-events')
API_KEY = os.getenv('API_KEY', '')
FETCH_INTERVAL = int(os.getenv('FETCH_INTERVAL', 15))

