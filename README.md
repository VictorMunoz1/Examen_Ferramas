Proyecto Ferramas
![image](https://github.com/user-attachments/assets/8d0d69ec-7da9-4ea2-95d6-6894de1db31e)

Lenguajes:
Python:Principal lenguaje utilizado para la lógica del backend.
![image](https://github.com/user-attachments/assets/dd4c0126-71b3-42b1-b604-92f347d5ec3a)

HTML, CSS, JavaScript: Utilizados para el frontend.
![image](https://github.com/user-attachments/assets/fa732556-56d1-4c19-8975-f06ed651f0e5)  ![image](https://github.com/user-attachments/assets/6ae20131-eeac-4c7b-a807-15970126f3d5)  ![image](https://github.com/user-attachments/assets/dd8cd794-3958-4583-ae7d-5105e57a8d5c)



Tecnología:
Flask
SendGrid
Bootstrap
DB (Base de Datos): MySQL
Arquitectura:
MVC (Modelo - Vista- Controlador)
Framework:
Flask
Pasos de Implementación:

Crear y Activar un Entorno Virtual:


python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
Instalar Dependencias:

pip install -r requirements.txt
Configurar Variables de Entorno:

Crear un archivo .env y agregar las variables necesarias, como configuraciones de la base de datos y claves API para servicios como SendGrid.
Inicializar la Base de Datos:

flask db init
flask db migrate -m "Initial migration."
flask db upgrade
Ejecutar la Aplicación:

flask run
Acceder a la Aplicación:

Abre tu navegador y ve a http://127.0.0.1:5000 para ver tu aplicación en funcionamiento.
<!---

--->
