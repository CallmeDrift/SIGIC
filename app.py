from flask import Flask, render_template
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
    return render_template('consulta.html')



if __name__ == '__main__':
    app.run(debug=True)
