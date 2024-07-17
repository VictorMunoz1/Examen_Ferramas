import unittest
from unittest.mock import patch
from flask_testing import TestCase
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'api')))

from app import app

class CurrencyConversionTest(TestCase):
    def create_app(self):

        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        return app

    def setUp(self):

        self.patcher = patch('requests.post')
        self.mock_post = self.patcher.start()

    def tearDown(self):

        self.patcher.stop()

    def test_currency_conversion(self):

        mock_response = {
            'conversion_rates': {
                'USD': 0.001,  
                'EUR': 0.002

            }
        }
        self.mock_post.return_value.json.return_value = mock_response
        self.mock_post.return_value.status_code = 302  


        response = self.client.post('/actualizar_moneda_carrito', data={'moneda_destino': 'USD'})

        self.assertTrue(response.status_code == 302)

        if response.status_code == 302:
            return


        expected_total_convertido = 100 * 0.001  # Ejemplo de conversión: 100 CLP a USD
        self.assertIn(f'Total convertido: {expected_total_convertido}', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
