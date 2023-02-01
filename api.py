from flask import Flask, jsonify, request

app = Flask(__name__)
SECRET_TOKEN = 'Basic secret_test_token' # embedded here only for exercise purpose

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

def check_auth(auth_header):
    if auth_header == SECRET_TOKEN:
        return True
    return False

@app.route('/stocks', methods=['GET'])
def get_stocks():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not check_auth(auth_header):
        return jsonify({'error': 'Unauthorized'}), 401
    return jsonify(STOCKS)

@app.route('/tickers/<string:ticker>/history', methods=['GET'])
def get_stock_history(ticker):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not check_auth(auth_header):
        return jsonify({'error': 'Unauthorized'}), 401
    
    ticker = ticker.upper()

    if ticker not in PRICES.keys():
        return jsonify({'error': 'Invalid ticker'}), 404

    data = get_last_90_days_prices(ticker)

    # sort in date descending order
    sorted_data = sorted(data, key=lambda x: x['date'], reverse=True)

    return jsonify(sorted_data)


if __name__ == '__main__':
    app.run()