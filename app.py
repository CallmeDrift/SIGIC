from flask import Flask, render_template
from database import get_connection

# ESTE PROYECTO UTILIZA FLASK, EJECÚTALO CON EL COMANDO PYTHON app.py
app = Flask(__name__)


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

@app.route('/login')
def login():
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
    return render_template('gestionproductos.html')

@app.route('/agregarproducto')
def agregarproducto():
    return render_template('AgregarProducto.html')

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
