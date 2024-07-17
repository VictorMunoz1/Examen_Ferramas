import unittest
from flask import url_for
from app import app, db, cursor  # Asegúrate de importar tu aplicación y configuración necesaria

class TestSuscripcion(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.db = db  # Asegúrate de inicializar tu conexión a la base de datos aquí
        self.cursor = cursor  # Asegúrate de inicializar tu cursor aquí

    def test_registro_nuevo_suscriptor(self):
        with self.app as client:
            # Realiza una solicitud POST simulada a la ruta '/suscribirse'
            response = client.post('/suscribirse', data={'email': 'test@example.com'})

            # Verifica que la respuesta sea una redirección (código 302)
            self.assertEqual(response.status_code, 302)
            
            # Puedes agregar más validaciones si deseas asegurarte de que la redirección sea a la página correcta
            self.assertTrue(response.location.endswith(url_for('home')))

if __name__ == '__main__':
    unittest.main()
