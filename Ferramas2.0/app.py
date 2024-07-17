import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, session, flash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions
import requests
import time

# Configuración de la conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="victor",
    password="duoc",
    database="bd_ferramas"
)
cursor = db.cursor()

app = Flask(__name__)
app.secret_key = 'duoc'

SENDGRID_API_KEY = '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'
SENDER_EMAIL = 'vic.munozd@duocuc.cl'

commerce_code = '597055555532'
api_key = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
transbank_options = WebpayOptions(commerce_code, api_key, "https://webpay3gint.transbank.cl")

EXCHANGERATE_API_KEY = '0036ba23608df36e76810279'
EXCHANGERATE_URL = f'https://v6.exchangerate-api.com/v6/0036ba23608df36e76810279/latest/CLP'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            error = 'El nombre de usuario ya está en uso. Por favor, elige otro.'
            return render_template('register.html', error=error)

        insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(insert_query, (username, password))
        db.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            session['user_id'] = user[0]
            return redirect(url_for('home'))
        else:
            error = 'Credenciales inválidas. Por favor, inténtalo de nuevo.'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/materiales')
def materiales():
    cursor.execute("SELECT id, nombre, precio, stock, imagen_url FROM productos WHERE categoria = 'materiales'")
    productos = cursor.fetchall()
    return render_template('materiales.html', productos=productos)

@app.route('/epp')
def epp():
    cursor.execute("SELECT id, nombre, precio, stock, imagen_url FROM productos WHERE categoria = 'epp'")
    productos = cursor.fetchall()
    return render_template('epp.html', productos=productos)

@app.route('/herramientas')
def herramientas():
    cursor.execute("SELECT id, nombre, precio, stock, imagen_url FROM productos WHERE categoria = 'herramientas'")
    productos = cursor.fetchall()
    return render_template('herramientas.html', productos=productos)

@app.route('/tornillos_anclajes')
def tornillos_anclajes():
    cursor.execute("SELECT id, nombre, precio, stock, imagen_url FROM productos WHERE categoria = 'Tornillos y Anclajes'")
    productos = cursor.fetchall()
    return render_template('tornillos_anclajes.html', productos=productos)

@app.route('/fijaciones')
def fijaciones():
    cursor.execute("SELECT id, nombre, precio, stock, imagen_url FROM productos WHERE categoria = 'Fijaciones'")
    productos = cursor.fetchall()
    return render_template('fijaciones.html', productos=productos)


@app.route('/equipos_medicion')
def equipos_medicion():
    cursor.execute("SELECT id, nombre, precio, stock, imagen_url FROM productos WHERE categoria = 'Equipos de Medición'")
    productos = cursor.fetchall()
    return render_template('equipos_medicion.html', productos=productos)


@app.route('/api')
def api():
    return render_template('api.html')

def obtener_productos():
    cursor.execute("SELECT id, nombre, precio, stock, imagen_url FROM productos")
    return cursor.fetchall()

@app.route('/agregar_al_carrito', methods=['POST'])
def agregar_al_carrito():
    if 'carrito' not in session:
        session['carrito'] = []

    producto_id = request.form.get('producto_id')
    cantidad = int(request.form.get('cantidad', 1))

    cursor.execute("SELECT id, nombre, precio, stock, imagen_url FROM productos WHERE id = %s", (producto_id,))
    producto = cursor.fetchone()

    if producto and producto[3] >= cantidad:
        item = {
            'id': producto[0],
            'nombre': producto[1],
            'precio': float(producto[2]),
            'cantidad': cantidad,
            'imagen_url': producto[4]
        }
        session['carrito'].append(item)
        flash(f"Se ha agregado '{producto[1]}' al carrito", 'success')
    else:
        flash('Cantidad solicitada no disponible en stock', 'error')

    return redirect(url_for('ver_carrito'))

@app.route('/carrito')
def ver_carrito():
    carrito = session.get('carrito', [])
    moneda_destino = session.get('moneda_destino', 'CLP')
    total = sum(float(item['precio']) * int(item['cantidad']) for item in carrito)

    if moneda_destino != 'CLP':
        response = requests.get(EXCHANGERATE_URL)
        datos_conversion = response.json()
        if response.status_code == 200:
            tasa_conversion = datos_conversion['conversion_rates'].get(moneda_destino, 1)
            total_convertido = total * tasa_conversion
            for item in carrito:
                item['precio_convertido'] = float(item['precio']) * tasa_conversion  # Convertimos a float
        else:
            flash('Error al obtener la tasa de conversión.', 'error')
            total_convertido = total
            moneda_destino = 'CLP'
    else:
        total_convertido = total

    return render_template('carrito.html', carrito=carrito, total_convertido=total_convertido, moneda_actual='CLP', moneda_destino=moneda_destino)

@app.route('/actualizar_moneda_carrito', methods=['POST'])
def actualizar_moneda_carrito():
    moneda_destino = request.form['moneda_destino']
    session['moneda_destino'] = moneda_destino
    return redirect(url_for('ver_carrito'))

@app.route('/limpiar_carrito')
def limpiar_carrito():
    session.pop('carrito', None)
    session.pop('moneda_destino', None)  # Limpiar también la moneda destino
    flash('Se ha limpiado el carrito', 'info')
    return redirect(url_for('home'))

@app.route('/')
def home():
    cursor.execute("SELECT id, nombre, precio, stock, imagen_url FROM productos")
    productos = cursor.fetchall()
    return render_template('home.html', productos=productos)

@app.route('/suscribirse', methods=['POST'])
def suscribirse():
    email = request.form['email']

    cursor.execute("SELECT * FROM suscriptores WHERE email = %s", (email,))
    existing_subscriber = cursor.fetchone()

    if existing_subscriber:
        flash('Este correo electrónico ya está suscrito.', 'warning')
        return redirect(url_for('home'))

    cursor.execute("INSERT INTO suscriptores (email) VALUES (%s)", (email,))
    db.commit()

    message = Mail(
        from_email=SENDER_EMAIL,
        to_emails=email,
        subject='Confirmación de suscripción',
        html_content='<strong>Gracias por suscribirte a nuestro boletín <3.</strong>'
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))

    flash('Te has suscrito correctamente. Por favor, verifica tu correo electrónico para confirmar la suscripción.', 'success')
    return redirect(url_for('home'))

@app.route('/checkout', methods=['POST'])
def checkout():
    carrito = session.get('carrito', [])
    moneda_destino = session.get('moneda_destino', 'CLP')
    total = sum(float(item['precio']) * int(item['cantidad']) for item in carrito)

    if moneda_destino != 'CLP':
        response = requests.get(EXCHANGERATE_URL)
        datos_conversion = response.json()
        if response.status_code == 200:
            tasa_conversion = datos_conversion['conversion_rates'].get(moneda_destino, 1)
            total = total * tasa_conversion
        else:
            flash('Error al obtener la tasa de conversión.', 'error')
            app.logger.error('Error al obtener la tasa de conversión: %s', response.text)

    buy_order = str(session.get('user_id', '')) + str(int(time.time()))

    transaction = Transaction(transbank_options)
    try:
        response = transaction.create(
            buy_order=buy_order,
            session_id=str(session.get('user_id', '')),
            amount=total,
            return_url=url_for('pago_exitoso', _external=True)
        )
        app.logger.info('Respuesta de creación de transacción: %s', response)
        
        if 'token' in response and response['token']:
            return redirect(response['url'] + '?token_ws=' + response['token'])
        else:
            flash('Error al procesar el pago: no se recibió un token de Webpay.', 'error')
            app.logger.error('Error al procesar el pago: no se recibió un token de Webpay.')
            return redirect(url_for('ver_carrito'))
    except Exception as e:
        flash('Error al procesar el pago: {}'.format(str(e)), 'error')
        app.logger.error('Error al procesar el pago: %s', str(e))
        return redirect(url_for('ver_carrito'))

@app.route('/pago_exitoso', methods=['GET', 'POST'])
def pago_exitoso():
    print("Entrando a la ruta de pago_exitoso")
    app.logger.info("Entrando a la ruta de pago_exitoso")
    
    if request.method == 'POST':
        print("Recibida solicitud POST")
        app.logger.info("Recibida solicitud POST")
        
        token = request.form.get('token_ws')
        print("Token recibido:", token)
        app.logger.info("Token recibido: %s", token)
        
        transaction = Transaction(transbank_options)
        try:
            response = transaction.commit(token)
            app.logger.info('Respuesta de transacción: %s', response)
            if response['status'] == 'AUTHORIZED':
                reducir_stock()
                session.pop('carrito', None)
                session.pop('moneda_destino', None)  # Limpiar también la moneda destino
                flash('Pago realizado con éxito.', 'success')
            else:
                flash('Hubo un problema con el pago.', 'error')
        except Exception as e:
            flash('Error al confirmar el pago: {}'.format(str(e)), 'error')
        return redirect(url_for('home'))
    
    print("Solicitud no es POST")
    app.logger.info("Solicitud no es POST")
    
    flash('Método no permitido.', 'error')
    return redirect(url_for('home'))




def reducir_stock():
    carrito = session.get('carrito', [])
    for item in carrito:
        cursor.execute("UPDATE productos SET stock = stock - %s WHERE id = %s", (item['cantidad'], item['id']))
    db.commit()




if __name__ == '__main__':
    app.run(debug=True)

