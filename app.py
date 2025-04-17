from flask import Flask, render_template

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Rutas para cada sección
@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/cabecera')
def cabecera():
    return render_template('cabecera.html')

@app.route('/comunicados')
def comunicados():
    return render_template('comunicados.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/consulta')
def inventario():
    return '<h2>Aquí va la consulta 🚀</h2>'

@app.route('/caja')
def caja():
    return '<h2>Aquí va la caja 💸</h2>'


if __name__ == '__main__':
    app.run(debug=True)
