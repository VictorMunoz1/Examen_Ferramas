import unittest
from unittest.mock import patch, MagicMock
from flask_testing import TestCase
import sys
import os

# Añadir el directorio del proyecto al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'api')))

from app import app

class MyTest(TestCase):
    def create_app(self):
        # Configurar aplicación Flask para los tests
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        return app

    def setUp(self):
        # Parchar el método connect de MySQLdb
        self.patcher = patch('MySQLdb.connect')
        self.mock_connect = self.patcher.start()
        
        # Crear mocks para la conexión y el cursor
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_connect.return_value = self.mock_connection
        self.mock_connection.cursor.return_value = self.mock_cursor
        
        # Configurar el cursor mock para que devuelva datos de prueba
        self.mock_cursor.execute.return_value = None
        self.mock_cursor.fetchall.return_value = [
            {"id": 4, "nombre": "Sacos de Cemento", "precio": 10000.00, "stock": 60, "categoria": "materiales", "imagen_url": "https://construmartcl.vtexassets.com/arquivos/ids/206706/198442_1.jpg?v=638289210428800000"},
            {"id": 5, "nombre": "Tablas de Madera", "precio": 8000.00, "stock": 100, "categoria": "materiales", "imagen_url": "https://static.wixstatic.com/media/5afc50_cd075b160f53471ca1363269909ecd2a~mv2.jpg/v1/fill/w_560,h_400,al_c,q_80,enc_auto/5afc50_cd075b160f53471ca1363269909ecd2a~mv2.jpg"}
        ]
        self.mock_cursor.description = [
            ('id',), ('nombre',), ('precio',), ('stock',), ('categoria',), ('imagen_url',)
        ]

    def tearDown(self):
        # Detener el parche
        self.patcher.stop()

    def test_materiales(self):
        response = self.client.get('/materiales')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Sacos de Cemento', response.data.decode())
        self.assertIn('Tablas de Madera', response.data.decode())

if __name__ == '__main__':
    unittest.main()
