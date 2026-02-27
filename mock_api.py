from flask import Flask, jsonify, request
import random

app = Flask(__name__)

CITIES = ['mum', 'dlh', 'chn', 'bng']
FUEL_TYPES = ['Petrol', 'Diesel']

@app.route('/v1/prices')
def prices():
    _ = request.args.get('apikey')  # ignored in mock
    city_param = request.args.get('cities')
    cities = city_param.split(',') if city_param else CITIES
    data = {"prices": []}
    for city in cities:
        for fuel in FUEL_TYPES:
            base = 105 if fuel == 'Petrol' else 95
            price = round(base + random.uniform(-1.0, 1.0), 2)
            data["prices"].append({
                "city": city,
                "fuel_type": fuel,
                "price": price
            })
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
