import unittest
import requests
import random

from requests.auth import HTTPBasicAuth
from settings import AVAILABLE_TICKERS, TICKER_SEEDS, USERS, USERS_PORTFOLIO

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.url = 'http://localhost:5000'

    def test_get_stocks_success(self):
        username = 'john'
        correct_data = []
        for stock in USERS_PORTFOLIO[username]:
            random.seed(TICKER_SEEDS[stock])
            correct_data.append(
                {
                    'symbol': stock,
                    'price': random.random()
                }
            )
        response = requests.get(f'{self.url}/stocks', auth=HTTPBasicAuth('john', ''))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), correct_data)

    def test_get_stocks_unauthorized(self):
        response = requests.get(f'{self.url}/stocks')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'error': 'Unauthorized'})

    def test_get_stock_history(self):
        response = requests.get(f'{self.url}/tickers/AAPL/history', auth=HTTPBasicAuth('john', ''))
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_get_stock_history_unauthorized(self):
        response = requests.get(f'{self.url}/tickers/AAPL/history')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'error': 'Unauthorized'})

    def test_get_stock_history_invalid_ticker(self):
        response = requests.get(f'{self.url}/tickers/INVALID/history', auth=HTTPBasicAuth('paul', ''))
        self.assertEqual(response.status_code, 404)
    
    def test_get_stock_history_same_data_different_user(self):
        response_john = requests.get(f'{self.url}/tickers/goog/history', auth=HTTPBasicAuth('john', ''))
        response_mike = requests.get(f'{self.url}/tickers/goog/history', auth=HTTPBasicAuth('mike', ''))
       
        self.assertEqual(response_john.json(), response_mike.json())

if __name__ == '__main__':
    unittest.main()
