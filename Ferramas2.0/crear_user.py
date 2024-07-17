import unittest
import requests

class TestUsuario(unittest.TestCase):
    
    def setUp(self):
        # Configurar la aplicación Flask en modo de prueba
        from app import app, db, cursor  
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  
        self.app = app.test_client()
        self.db = db
        self.cursor = cursor

    def tearDown(self):
        # Limpiar la base de datos después de cada test
        self.cursor.execute("DELETE FROM users WHERE username LIKE 'test_user%'")
        self.db.commit()

    def test_registro_nuevo_usuario(self):

        new_username = 'test_user'
        new_password = 'test_password'


        response = self.app.post('/register', data={
            'username': new_username,
            'password': new_password
        })


        self.assertEqual(response.status_code, 302)  # Esperamos una redirección después del registro


        self.cursor.execute("SELECT * FROM users WHERE username = %s", (new_username,))
        created_user = self.cursor.fetchone()
        self.assertIsNotNone(created_user)  # Aseguramos que el usuario fue creado

if __name__ == '__main__':
    unittest.main()
