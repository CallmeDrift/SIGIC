from flask import Flask, render_template, request, redirect, flash, session
from database import get_connection

# ESTE PROYECTO UTILIZA FLASK, EJECÚTALO CON EL COMANDO PYTHON app.py
app = Flask(__name__)
app.secret_key = 'Clave.77'  # Debo recordar cambiar esta clave por una más segura en producción


# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Rutas para cada sección 
@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/cabecera')
def cabecera():
    return render_template('cabecera.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario = %s", (usuario,))
        user = cursor.fetchone()
        conn.close()

        if user and user['contraseña'] == contraseña:
            session['usuario'] = user['nombre_usuario']
            return redirect('/admin')
        else:
            return render_template('LoginAdmin.html', error="Usuario o contraseña incorrectos 😓")

    return render_template('LoginAdmin.html')


@app.route('/comunicados')
def comunicados():
    return render_template('comunicados.html')

@app.route('/caja')
def caja():
    return render_template('caja.html')

@app.route('/consulta')
def inventario():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")  # Ajusta según columnas reales
    productos = cursor.fetchall()
    conn.close()
    return render_template('consulta.html', productos=productos)

@app.route('/ayuda')
def ayuda():
    return render_template('ayuda.html')

@app.route('/gestionproductos')
def gestionproductos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nombre_producto, precio_venta, cantidad FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return render_template('gestionproductos.html', productos=productos)

@app.route('/agregarproducto', methods=['GET', 'POST'])
def agregarproducto():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        nombre = request.form['nombre_producto']
        codigo = request.form['codigo']
        precio_compra = float(request.form['precio_compra'])
        precio_venta = round(precio_compra * 1.2, 2)
        precio_mayor = round(precio_compra * 1.1, 2)  # (aún no se usa en DB pero ya lo tienes calculado)
        descripcion = request.form.get('descripcion', '')
        presentacion = request.form.get('presentacion', '')
        ubicacion = request.form.get('ubicacion', '')
        stock = int(request.form['cantidad'])
        proveedor = request.form.get('id_proveedor')

        # Insertar producto
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO productos 
            (nombre_producto, codigo, precio_compra, precio_venta, descripcion, presentacion, ubicacion, cantidad, id_proveedor)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (nombre, codigo, precio_compra, precio_venta, descripcion, presentacion, ubicacion, stock, proveedor))

        conn.commit()
        conn.close()
        return redirect('/gestionproductos')

    # Si es GET, cargar proveedores
    cursor.execute("SELECT id, empresa FROM proveedores")
    proveedores = cursor.fetchall()
    conn.close()
    return render_template('AgregarProducto.html', proveedores=proveedores)


@app.route('/editarproducto')
def editarproducto():
    return render_template('EditarProducto.html')

@app.route('/gestionproveedores')
def gestionproveedores():
    return render_template('gestionproveedores.html')

@app.route('/agregarproveedor')
def agregarproveedor(): 
    return render_template('AgregarProveedor.html')

@app.route('/editarproveedor')
def editarproveedor():
    return render_template('EditarProveedor.html')

@app.route('/gestionclientes')
def gestionclientes():
    return render_template('gestionClientes.html')

@app.route('/agregarcliente')
def agregarcliente():
    return render_template('AgregarClientes.html')

@app.route('/editarcliente')
def editarcliente():
    return render_template('EditarClientes.html')

if __name__ == '__main__':
    app.run(debug=True)
