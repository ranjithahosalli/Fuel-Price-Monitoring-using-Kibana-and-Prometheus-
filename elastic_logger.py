import os
from elasticsearch import Elasticsearch, helpers

class ElasticLogger:
    def __init__(self):
        self.elastic_url = os.getenv('ELASTIC_URL', 'http://localhost:9200')
        self.index = os.getenv('ELASTIC_INDEX', 'fuel-price-events')
        self.enabled = False
        try:
            self.es = Elasticsearch(self.elastic_url, verify_certs=False)
            # Try a health check
            if self.es.ping():
                self.enabled = True
                self._ensure_index()
        except Exception as e:
            print(f"[ElasticLogger] Elasticsearch not available: {e}")
            self.enabled = False

    def _ensure_index(self):
        try:
            if not self.es.indices.exists(index=self.index):
                mapping = {
                    "mappings": {
                        "properties": {
                            "city": {"type": "keyword"},
                            "fuel_type": {"type": "keyword"},
                            "price": {"type": "float"},
                            "timestamp": {"type": "date", "format": "strict_date_optional_time||epoch_millis"}
                        }
                    }
                }
                self.es.indices.create(index=self.index, body=mapping)
        except Exception as e:
            print(f"[ElasticLogger] Failed ensuring index mapping: {e}")

    def log_price_updates(self, fuel_prices):
        if not self.enabled:
            return
        actions = [
            {
                "_index": self.index,
                "_source": {
                    "city": fp.city,
                    "fuel_type": fp.fuel_type,
                    "price": fp.price,
                    "timestamp": (fp.timestamp.isoformat() + 'Z')
                }
            } for fp in fuel_prices]
        try:
            helpers.bulk(self.es, actions)
        except Exception as e:
            print(f"[ElasticLogger] Error logging to ES: {e}")

