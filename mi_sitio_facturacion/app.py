
from flask import Flask, render_template, g
import sqlite3
import os

app = Flask(__name__, template_folder='.')

DATABASE = os.path.join(os.path.dirname(__file__), 'facturacion.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/clientes")
def clientes():
    db = get_db()
    cur = db.execute("SELECT * FROM cliente")
    clientes = cur.fetchall()
    return render_template("clientes.html", clientes=clientes)

@app.route("/producto")
def producto():
    db = get_db()
    cur = db.execute("SELECT * FROM producto")
    productos = cur.fetchall()
    return render_template("producto.html", productos=productos)

@app.route("/categoria")
def categoria():
    db = get_db()
    cur = db.execute("SELECT * FROM categoria")
    categorias = cur.fetchall()
    return render_template("categoria.html", categorias=categorias)

@app.route("/empleado")
def empleado():
    db = get_db()
    cur = db.execute("SELECT * FROM empleado")
    empleados = cur.fetchall()
    return render_template("empleado.html", empleados=empleados)

@app.route("/proveedor")
def proveedor():
    db = get_db()
    cur = db.execute("SELECT * FROM proveedor")
    proveedores = cur.fetchall()
    return render_template("proveedor.html", proveedores=proveedores)

if __name__ == "__main__":
    app.run(debug=True)
