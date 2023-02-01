import unittest
import requests

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.url = 'http://localhost:5000'
        self.headers = {'Authorization': 'Basic secret_test_token'}

    def test_get_stocks_success(self):
        correct_data = [
            {'price': 100.0, 'symbol': 'aapl'},
            {'price': 200.0, 'symbol': 'amzn'},
            {'price': 300.0, 'symbol': 'tsla'}
        ]
        response = requests.get(f'{self.url}/stocks', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), correct_data)

    def test_get_stocks_unauthorized(self):
        response = requests.get(f'{self.url}/stocks')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'error': 'Unauthorized'})

    def test_get_stock_history(self):
        response = requests.get(f'{self.url}/tickers/AAPL/history', headers=self.headers)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_get_stock_history_unauthorized(self):
        response = requests.get(f'{self.url}/tickers/AAPL/history')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'error': 'Unauthorized'})

    def test_get_stock_history_invalid_ticker(self):
        response = requests.get(f'{self.url}/tickers/INVALID/history', headers=self.headers)
        self.assertEqual(response.status_code, 404)
    
    def test_get_stock_history_date_descending_order(self):
        response = requests.get(f'{self.url}/tickers/aapl/history', headers=self.headers)
        correct_data = [
            {
                'date': '2023-01-31',
                'price': '100'
            },
            {
                'date': '2023-01-30',
                'price': '99.86'
            }
        ]
        self.assertEqual(response.json(), correct_data)


if __name__ == '__main__':
    unittest.main()
