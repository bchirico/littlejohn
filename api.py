from flask import Flask, jsonify, request

app = Flask(__name__)
SECRET_TOKEN = 'Basic secret_test_token' # embedded here only for exercise purpose

stocks = [
    {'price': 100.0, 'symbol': 'aapl'},
    {'price': 200.0, 'symbol': 'amzn'},
    {'price': 300.0, 'symbol': 'tsla'}
]

def check_auth(auth_header):
    if auth_header == SECRET_TOKEN:
        return True
    return False

@app.route('/stocks', methods=['GET'])
def get_stocks():
    auth_header = request.headers.get('Authorization')
    print(auth_header)
    if not auth_header or not check_auth(auth_header):
        return jsonify({'error': 'Unauthorized'}), 401
    return jsonify(stocks)

if __name__ == '__main__':
    app.run()