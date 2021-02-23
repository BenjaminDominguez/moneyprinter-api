from flask import Flask, jsonify
from datetime import datetime

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
def capital():
    capital_balances = [
    {
        'capital': 20,
        'utc_time': datetime.utcnow()
    },
    {
        'capital': 21,
        'utc_time': datetime.utcnow()
    },
    {
        'capital': 22,
        'utc_time': datetime.utcnow()
    },
    {
        'capital': 23,
        'utc_time': datetime.utcnow()
    }
    ]
    return jsonify(capital_balances)