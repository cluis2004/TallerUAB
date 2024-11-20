import bcrypt
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
        
        # Obtener la contraseña encriptada desde la base de datos
        query = "SELECT id, contrasena FROM perfiles WHERE correo_electronico = %s"
        cursor.execute(query, (correo_electronico,))
        user = cursor.fetchone()

        if user:
            user_id, hashed_password = user
            # Verificar la contraseña ingresada contra el hash almacenado
            if bcrypt.checkpw(contrasena.encode('utf-8'), hashed_password.encode('utf-8')):
                print(f"Inicio de sesión exitoso para el usuario con ID: {user_id}")
                return user_id
            else:
                print("Credenciales inválidas")
                return None
        else:
            print("Usuario no encontrado")
            return None
    except Exception as e:
        print(f"Error al iniciar sesión: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
