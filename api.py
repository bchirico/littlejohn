from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

SECRET_TOKEN = 'Basic secret_test_token' # embedded here only for exercise purpose

AVAILABLE_TICKERS = [
    "AAPL",
    "MSFT",
    "GOOG",
    "AMZN",
    "FB",
    "TSLA",
    "NVDA",
    "JPM",
    "BABA",
    "JNJ",
    "WMT",
    "PG",
    "PYPL",
    "DIS",
    "ADBE",
    "PFE",
    "V",
    "MA",
    "CRM",
    "NFLX"
]

SEEDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

TICKER_SEEDS = dict(zip(AVAILABLE_TICKERS, SEEDS))

print(TICKER_SEEDS)

USERS = [
    'john',
    'mike',
    'paul'
]

STOCKS = [
    {'price': 100.0, 'symbol': 'aapl'},
    {'price': 200.0, 'symbol': 'amzn'},
    {'price': 300.0, 'symbol': 'tsla'}
]
 
PRICES = {
    'AAPL': [
        {
            'date': '2023-01-31',
            'price': '100'
        },
        {
            'date': '2023-01-30',
            'price': '99.86'
        }
    ]
}

def get_last_90_days_prices(ticker):
    # make a request to a stock price provider
    # here I will make a fake function that returns only 90 days prices
    # response = requests.get(f'https://some-stock-price-api.com/{ticker}/history')
    # data = response.json()

    return PRICES[ticker]

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
    return jsonify(STOCKS)

@app.route('/tickers/<string:ticker>/history', methods=['GET'])
@auth.login_required
def get_stock_history(ticker):
    ticker = ticker.upper()

    if ticker not in AVAILABLE_TICKERS:
        return jsonify({'error': 'Invalid ticker'}), 404

    data = get_last_90_days_prices(ticker)

    # sort in date descending order
    sorted_data = sorted(data, key=lambda x: x['date'], reverse=True)

    return jsonify(sorted_data)


if __name__ == '__main__':
    app.run()