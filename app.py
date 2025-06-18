from flask import Flask, render_template, request, redirect, flash, session
from database import get_connection
from decimal import Decimal

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



@app.route('/caja', methods=['GET', 'POST'])
def caja():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        id_cliente = request.form['cliente_id']
        productos = eval(request.form['productos'])  # eval solo si confías en el input

        total_venta = sum([p['total'] for p in productos])

        cursor.execute("""
            INSERT INTO ventas (fecha_venta, total_venta, id_usuario, id_cliente)
            VALUES (CURDATE(), %s, %s, %s)
        """, (total_venta, 1, id_cliente))
        id_venta = cursor.lastrowid

        for producto in productos:
            cursor.execute("""
                INSERT INTO detallesventas (id_producto, id_cliente, cantidad, valor_unitario, valor_total, fecha, id_venta)
                VALUES (%s, %s, %s, %s, %s, CURDATE(), %s)
            """, (
                producto['id'], id_cliente, producto['cantidad'],
                producto['precio_venta'], producto['total'], id_venta
            ))

            cursor.execute("""
                UPDATE productos
                SET cantidad = cantidad - %s
                WHERE id = %s
            """, (producto['cantidad'], producto['id']))

        conn.commit()
        conn.close()
        return redirect('/caja')

    cursor.execute("SELECT id, nombre FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return render_template('caja.html', clientes=clientes)

@app.route('/buscarproducto')
def buscarproducto():
    query = request.args.get('query', '')
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, nombre_producto, codigo, precio_venta
        FROM productos
        WHERE cantidad > 0 AND (nombre_producto LIKE %s OR codigo LIKE %s)
        LIMIT 10
    """, (f"%{query}%", f"%{query}%"))
    resultados = cursor.fetchall()
    conn.close()

    return {'productos': resultados}

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
    cursor.execute("SELECT * FROM productos")
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


@app.route('/editarproducto/<int:id>', methods=['GET', 'POST'])
def editarproducto(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    print("Método:", request.method)

    if request.method == 'POST':
        nombre_producto = request.form['nombre_producto']
        precio_compra = float(request.form['precio_compra'])
        cantidad = int(request.form['cantidad'])
        descripcion = request.form['descripcion']
        codigo = request.form['codigo']
        presentacion = request.form['presentacion']
        ubicacion = request.form['ubicacion']
        id_proveedor = int(request.form['id_proveedor'])
        precio_venta = precio_compra * 1.2  # Mismo cálculo de antes

        cursor.execute("""
            UPDATE productos
            SET nombre_producto=%s, precio_compra=%s, precio_venta=%s, cantidad=%s,
                descripcion=%s, codigo=%s, presentacion=%s, ubicacion=%s, id_proveedor=%s
            WHERE id=%s
        """, (nombre_producto, precio_compra, precio_venta, cantidad,
              descripcion, codigo, presentacion, ubicacion, id_proveedor, id))
        
        conn.commit()
        conn.close()
        return redirect('/gestionproductos')

    # GET: mostrar datos en el formulario
    cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
    producto = cursor.fetchone()
    conn.close()

    if not producto:
        return "Producto no encontrado", 404

    precio_compra = producto["precio_compra"]
    precio_mayor = precio_compra * Decimal('1.1')
    precio_unidad = precio_compra * Decimal('1.2')

    conn.close()
    return render_template("EditarProducto.html",
                           producto=producto,
                           precio_mayor=precio_mayor,
                           precio_unidad=precio_unidad)


@app.route('/eliminarproducto/<int:id>', methods=['POST'])
def eliminar_producto(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect('/gestionproductos')

@app.route('/gestionproveedores')
def gestion_proveedores():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM proveedores")
    proveedores = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('gestionproveedores.html', proveedores=proveedores)

@app.route('/agregarproveedor', methods=['GET', 'POST'])
def agregarproveedor():
    if request.method == 'POST':
        nombre = request.form['nombre']
        empresa = request.form['empresa']
        contacto = request.form['contacto']
        telefono2 = request.form.get('telefono2') or None  # Aquí está la magia

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO proveedores (nombre, empresa, contacto, telefono2)
                VALUES (%s, %s, %s, %s)
            """, (nombre, empresa, contacto, telefono2))
            conn.commit()
            conn.close()
            return redirect('/gestionproveedores')
        except Exception as e:
            print("Error agregando proveedor:", e)
            return "Ocurrió un error agregando el proveedor. Revisá consola."

    return render_template('agregarproveedor.html')

@app.route('/editarproveedor/<int:id>', methods=['GET', 'POST'])
def editarproveedor(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        nombre = request.form['nombre']
        empresa = request.form['empresa']
        contacto = request.form['contacto']

        cursor.execute("""
            UPDATE proveedores
            SET nombre = %s, empresa = %s, contacto = %s
            WHERE id = %s
        """, (nombre, empresa, contacto, id))

        conn.commit()
        conn.close()
        return redirect('/gestionproveedores')

    # GET: Mostrar datos actuales en el formulario
    cursor.execute("SELECT * FROM proveedores WHERE id = %s", (id,))
    proveedor = cursor.fetchone()
    conn.close()

    if not proveedor:
        return "Proveedor no encontrado", 404

    return render_template('editarproveedor.html', proveedor=proveedor)

@app.route('/eliminarproveedor/<int:id>', methods=['POST', 'GET'])
def eliminarproveedor(id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM proveedores WHERE id = %s", (id,))
        conn.commit()
    except Exception as e:
        print(f"Error eliminando proveedor: {e}")
    finally:
        conn.close()

    return redirect('/gestionproveedores')



@app.route('/gestionclientes')
def gestion_clientes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('gestionClientes.html', clientes=clientes)

@app.route('/agregarcliente', methods=['GET', 'POST'])
def agregarcliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        cedula = request.form['cedula']
        contacto = request.form['contacto']

        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                    INSERT INTO clientes (nombre, apellido, cedula, contacto)
                    VALUES (%s, %s, %s, %s)
                """, (nombre, apellido, cedula, contacto))
            conn.commit()
        except Exception as e:
            print("Error al insertar cliente:", e)
            conn.rollback()
            return "Ocurrió un error agregando el cliente. Revisá consola."
        finally:
            cursor.close()
            conn.close()

        return redirect('/gestionclientes')

    return render_template('AgregarClientes.html')

@app.route('/editarcliente/<int:id>', methods=['GET', 'POST'])
def editarcliente(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        cedula = request.form['cedula']
        contacto = request.form['contacto']

        cursor.execute("""
            UPDATE clientes
            SET nombre = %s, apellido = %s, cedula = %s, contacto = %s
            WHERE id = %s
        """, (nombre, apellido, cedula, contacto, id))

        conn.commit()
        conn.close()
        return redirect('/gestionclientes')

    # GET: Mostrar datos actuales en el formulario
    cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
    cliente = cursor.fetchone()
    conn.close()

    if not cliente:
        return "Cliente no encontrado", 404

    return render_template('EditarClientes.html', cliente=cliente)

@app.route('/eliminarcliente/<int:id>', methods=['POST'])
def eliminarcliente(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
    conn.commit()

    cursor.close()
    conn.close()
    return redirect('/gestionclientes')


if __name__ == '__main__':
    app.run(debug=True)
