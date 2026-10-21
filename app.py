def iniciar_sesion(usuario, contrasena):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE user = '" + usuario + "' AND pass = '" + contrasena + "'"
    cursor.execute(query)
    return cursor.fetchone() is not None