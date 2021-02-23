from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/trades')
def trades():
    trades = [
        [{
            'asset': 'ETH',
            'side': 'BUY',
            'transaction_time': datetime.utcnow(),
            'purchase_amount_minus_commission': 20,
            'average_price_of_asset': 1700
        },
        {
            'asset': 'ETH',
            'side': 'SELL',
            'transaction_time': datetime.utcnow(),
            'sale_amount_minus_commission': 21,
            'average_price_of_asset': 1720
        }]
    ]
    return jsonify(trades)

@app.route('/capital')
def capital():
    capital_balances = [20, 21, 22, 23, 24, 25, 26, 27]
    return jsonify(capital_balances)