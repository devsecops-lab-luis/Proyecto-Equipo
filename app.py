import sqlite3
from ui import mostrar_menu

def iniciar_sesion(usuario, contrasena):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE user = '" + usuario + "' AND pass = '" + contrasena + "'"
    cursor.execute(query)
    return cursor.fetchone() is not None

def main():
    mostrar_menu()

if __name__ == "__main__":
    main()