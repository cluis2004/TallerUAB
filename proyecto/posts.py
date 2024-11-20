from db_connection import get_connection  # Asegúrate de que esta función esté correctamente importada

def create_post(user_id, contenido):
    """
    Inserta una nueva publicación en la base de datos usando el ID del usuario.
    Esta versión no depende de Flask y el user_id debe pasarse explícitamente.
    """
    if not user_id:
        print("Error: Usuario no autenticado.")
        return

    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO publicaiones (id_perfil, contenido)
        VALUES (%s, %s);
        """
        cursor.execute(query, (user_id, contenido))
        connection.commit()
        print("¡Publicación creada exitosamente!")
    except Exception as e:
        print(f"Error al crear la publicación: {e}")
    finally:
        cursor.close()
        connection.close()
