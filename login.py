from db_connection import get_connection

def login_user(correo_electronico, contrasena):
    """
    Autentica al usuario verificando su correo y contraseña.
    Si es exitoso, guarda el ID del usuario.
    """
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT id FROM perfiles WHERE correo_electronico = %s AND contrasena = %s"
        cursor.execute(query, (correo_electronico, contrasena))
        user = cursor.fetchone()

        if user:
            user_id = user[0]
            print(f"Inicio de sesión exitoso para el usuario con ID: {user_id}")
            return user_id
        else:
            print("Credenciales inválidas")
            return None
    except Exception as e:
        print(f"Error al iniciar sesión: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
