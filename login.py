import bcrypt
from db_connection import get_connection

# Variable global para almacenar el ID del usuario autenticado
current_user_id = None

def login_user(correo_electronico, contrasena):
    """
    Autentica al usuario verificando su correo y contraseña.
    Si es exitoso, guarda el ID del usuario.
    """
    global current_user_id
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
                current_user_id = user_id
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


def update_profile():
    """
    Actualiza el perfil del usuario autenticado.
    """
    global current_user_id
    if not current_user_id:
        print("Error: No hay un usuario autenticado.")
        return

    print("\n=== Actualizar Perfil ===")
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Obtener información actual del perfil
        query_check = "SELECT nombre, correo_electronico FROM perfiles WHERE id = %s;"
        cursor.execute(query_check, (current_user_id,))
        perfil = cursor.fetchone()

        if not perfil:
            print(f"No se encontró el perfil con ID: {current_user_id}")
            return

        # Mostrar información actual del perfil
        print("\nInformación actual del perfil:")
        print(f"Nombre: {perfil[0]}, Correo electrónico: {perfil[1]}")

        # Solicitar nuevos valores
        nuevo_nombre = input("Nuevo nombre (deja en blanco para no cambiar): ")
        nuevo_correo = input("Nuevo correo electrónico (deja en blanco para no cambiar): ")

        # Construir la consulta de actualización dinámicamente
        updates = []
        values = []

        if nuevo_nombre:
            updates.append("nombre = %s")
            values.append(nuevo_nombre)

        if nuevo_correo:
            updates.append("correo_electronico = %s")
            values.append(nuevo_correo)

        # Solo ejecutar si hay campos que actualizar
        if updates:
            query_update = f"UPDATE perfiles SET {', '.join(updates)} WHERE id = %s;"
            values.append(current_user_id)
            cursor.execute(query_update, tuple(values))
            connection.commit()
            print("¡Perfil actualizado exitosamente!")
        else:
            print("No se realizaron cambios.")

    except Exception as e:
        print(f"Error al actualizar el perfil: {e}")
    finally:
        cursor.close()
        connection.close()
