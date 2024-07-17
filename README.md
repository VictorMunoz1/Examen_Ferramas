# 🚀 **Proyecto Ferramas**

¡Bienvenido al proyecto Ferramas! A continuación, te presento una visión general de las tecnologías, la arquitectura y los pasos necesarios para implementar la aplicación.

## 📸 Captura de Pantalla del Proyecto

![Ferramas](https://github.com/user-attachments/assets/8d0d69ec-7da9-4ea2-95d6-6894de1db31e)

![image](https://github.com/user-attachments/assets/16097514-ed3b-4c76-82ce-9a7fdc623391)


![image](https://github.com/user-attachments/assets/58b42e8b-bcaf-41d0-a453-1719261006b1)


![image](https://github.com/user-attachments/assets/546694ff-2a53-43f3-a095-4a04cf86a695)


![image](https://github.com/user-attachments/assets/b6f8069b-4127-44a7-a256-73835ea48b65)


![image](https://github.com/user-attachments/assets/bc606942-1a57-4e89-9b00-541da981f44c)






## 🛠 Tecnologías Utilizadas

### **Lenguajes de Programación**

- **Python**: El principal lenguaje utilizado para la lógica del backend.  
  ![Python](https://github.com/user-attachments/assets/dd4c0126-71b3-42b1-b604-92f347d5ec3a)

- **HTML, CSS, JavaScript**: Tecnologías utilizadas para el desarrollo del frontend.  
  ![HTML](https://github.com/user-attachments/assets/fa732556-56d1-4c19-8975-f06ed651f0e5) ![CSS](https://github.com/user-attachments/assets/6ae20131-eeac-4c7b-a807-15970126f3d5) ![JavaScript](https://github.com/user-attachments/assets/dd8cd794-3958-4583-ae7d-5105e57a8d5c)

### **Tecnologías y Herramientas**

- **Flask**: Un microframework para Python que se utiliza para crear aplicaciones web.  
  ![Flask](https://github.com/user-attachments/assets/78fb8d98-02b9-43cb-8779-ed6024ce7fa6)

- **SendGrid**: Servicio para enviar correos electrónicos transaccionales y de marketing.  
  ![SendGrid](https://github.com/user-attachments/assets/78fb8d98-02b9-43cb-8779-ed6024ce7fa6)

- **Bootstrap**: Framework para diseñar interfaces web responsivas.  
  ![Bootstrap](https://github.com/user-attachments/assets/fa732556-56d1-4c19-8975-f06ed651f0e5)

- **MySQL**: Sistema de gestión de bases de datos relacional.  
  ![MySQL](https://github.com/user-attachments/assets/663248cb-bdd6-4064-8b8d-2a7d4ba1f0df)

## 🏗 Arquitectura del Proyecto

- **Modelo-Vista-Controlador (MVC)**: Una arquitectura de software que organiza el código en tres componentes: Modelo, Vista y Controlador.  
  ![MVC](https://example.com/mvc_image)

- **Framework**: Flask  
  ![Flask](https://github.com/user-attachments/assets/78fb8d98-02b9-43cb-8779-ed6024ce7fa6)

## 📝 Pasos de Implementación

1. **Crear y Activar un Entorno Virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate

Instalar Dependencias:

pip install -r requirements.txt
Configurar Variables de Entorno
Crea un archivo .env y agrega las variables necesarias, como configuraciones de la base de datos y claves API para servicios como SendGrid.

Inicializar la Base de Datos:

flask db init
flask db migrate -m "Initial migration."
flask db upgrade
Ejecutar la Aplicación

flask run
Acceder a la Aplicación
Abre tu navegador y visita http://127.0.0.1:5000 para ver tu aplicación en funcionamiento.
