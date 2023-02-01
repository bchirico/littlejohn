import unittest
import requests

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:5000/stocks"
        self.headers = {"Authorization": "Basic secret_test_token"}

    def test_get_stocks_success(self):
        correct_data = [
            {'price': 100.0, 'symbol': 'aapl'},
            {'price': 200.0, 'symbol': 'amzn'},
            {'price': 300.0, 'symbol': 'tsla'}
        ]
        response = requests.get(self.url, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), correct_data)

    def test_get_stocks_unauthorized(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"error": "Unauthorized"})

if __name__ == "__main__":
    unittest.main()
