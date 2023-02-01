import random
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from datetime import datetime, timedelta

from settings import AVAILABLE_TICKERS, TICKER_SEEDS, USERS, USERS_PORTFOLIO

app = Flask(__name__)
auth = HTTPBasicAuth()

def get_user_portfolio_last_prices(username):
    today = datetime.now()

    last_prices = []
    for stock in USERS_PORTFOLIO[username]:
        random.seed(TICKER_SEEDS[stock])
        last_prices.append(
            {
                'symbol': stock,
                'price': random.random()
            }
        )
    return last_prices

def get_ticker_history(ticker):
    random.seed(TICKER_SEEDS[ticker])
    today = datetime.now()
    prices = []
    for i in range(90):
        prices.append({
            'date': (today - timedelta(days=i)).strftime('%Y-%m-%d'),
            'price': random.random()

        })
    return prices
    
@auth.verify_password
def verify_password(username, password):
    if username in USERS and password == '':
        return True
    return False

@auth.error_handler
def unauthorized():
    return jsonify({'error': 'Unauthorized'}), 401

@app.route('/stocks', methods=['GET'])
@auth.login_required
def get_stocks():
    username = auth.current_user()
    data = get_user_portfolio_last_prices(username)
    return jsonify(data)

@app.route('/tickers/<string:ticker>/history', methods=['GET'])
@auth.login_required
def get_stock_history(ticker):
    ticker = ticker.upper()

    if ticker not in AVAILABLE_TICKERS:
        return jsonify({'error': 'Not Found'}), 404

    data = get_ticker_history(ticker)
    print(data)

    # sort in date descending order
    sorted_data = sorted(data, key=lambda x: x['date'], reverse=True)

    return jsonify(sorted_data)


if __name__ == '__main__':
    app.run()