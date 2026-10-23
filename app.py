from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/login")
def login():
    usuario = request.args.get("usuario")
    contrasena = request.args.get("contrasena")
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

  
    query = "SELECT * FROM users WHERE user = ? AND pass = ?"

    
    cursor.execute(query, (usuario, contrasena))
    return str(cursor.fetchone() is not None)

if __name__ == "__main__":
    app.run()