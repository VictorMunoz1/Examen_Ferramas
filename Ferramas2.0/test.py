import unittest
from unittest.mock import patch, MagicMock
from app import app

class PaymentAPITest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    @patch('app.Transaction')
    def test_payment_process(self, MockTransaction):
        mock_transaction_instance = MockTransaction.return_value
        mock_transaction_instance.create.return_value = {
            'token': 'mock_token',
            'url': 'https://mockurl.com'
        }
        

        response = self.app.post('/checkout', data={})
        

        self.assertEqual(response.status_code, 302)
        self.assertIn('https://mockurl.com?token_ws=mock_token', response.location)
        

        mock_transaction_instance.create.assert_called_once()

if __name__ == '__main__':
    unittest.main()
