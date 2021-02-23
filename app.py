from flask import Flask, jsonify
from datetime import datetime
import pymongo
from dotenv import load_dotenv
import os
import ssl

load_dotenv()

PYMONGO_USERNAME = os.getenv('PYMONGO_USERNAME')
PYMONGO_PASSWORD = os.getenv('PYMONGO_PASSWORD')

PYMONGO_DB_URL = f"mongodb+srv://{PYMONGO_USERNAME}:{PYMONGO_PASSWORD}@trades.cdsd5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(PYMONGO_DB_URL, ssl_cert_reqs=ssl.CERT_NONE)
db = client.development
trades = db.trades
capital = db.capital

app = Flask(__name__)

@app.route('/trades')
def trades():
    trades = [
        [{
            'asset': 'ETH',
            'side': 'BUY',
            'utc_transaction_time': datetime.utcnow(),
            'purchase_amount_minus_commission': 20,
            'average_price_of_asset': 1700
        },
        {
            'asset': 'ETH',
            'side': 'SELL',
            'utc_transaction_time': datetime.utcnow(),
            'sale_amount_minus_commission': 21,
            'average_price_of_asset': 1720
        }],
        [{
            'asset': 'ETH',
            'side': 'BUY',
            'utc_transaction_time': datetime.utcnow(),
            'purchase_amount_minus_commission': 20,
            'average_price_of_asset': 1700
        },
        {
            'asset': 'ETH',
            'side': 'SELL',
            'utc_transaction_time': datetime.utcnow(),
            'purchase_amount_minus_commission': 19,
            'average_price_of_asset': 1690
        }]
    ]
    return jsonify(trades)

@app.route('/capital')
def show_capital():

    capital_balances = list(capital.find({}))

    json_formatted_capital_balances = []
    for capital_balance in capital_balances:
        capital_balance['_id'] = str(capital_balance['_id'])
        json_formatted_capital_balances.append(capital_balance)

    return jsonify(json_formatted_capital_balances)