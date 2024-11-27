from db_connection import get_connection  # Asegúrate de que esta función esté correctamente importada

current_user_id = None  # Variable global para almacenar el ID del usuario autenticado

def nueva_publicacion(user_id, contenido):
    """
    Inserta una nueva publicación en la base de datos usando el ID del usuario.
    Esta versión no depende de Flask y el user_id debe pasarse explícitamente.
    """
    
    global current_user_id  # Necesitamos modificar la variable global current_user_id

    if not user_id:
        print("Error: Usuario no autenticado.")
        return

    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO publicaciones (id_perfil, contenido)
        VALUES (%s, %s);
        """
        cursor.execute(query, (user_id, contenido))
        connection.commit()
        print("¡Publicación creada exitosamente!")
        
        # Actualizamos el current_user_id después de crear la publicación
        current_user_id = user_id

    except Exception as e:
        print(f"Error al crear la publicación: {e}")
    finally:
        cursor.close()
        connection.close()

def eliminar_publicacion(user_id, post_id):
    """
    Elimina una publicación del usuario autenticado.
    Solo se puede eliminar la publicación si el usuario autenticado es el propietario de la misma.
    """    
    if not user_id:
        print("Error: Usuario no autenticado.")
        return

    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Verificar si la publicación existe y pertenece al usuario autenticado
        query_check = "SELECT id_perfil FROM publicaciones WHERE id_publicacion = %s"
        cursor.execute(query_check, (post_id,))
        result = cursor.fetchone()

        if result:
            post_user_id = result[0]
            if post_user_id == user_id:
                # Eliminar la publicación si el usuario es el propietario
                query_delete = "DELETE FROM publicaciones WHERE id_publicacion = %s"
                cursor.execute(query_delete, (post_id,))
                connection.commit()
                print("¡Publicación eliminada exitosamente!")
            else:
                print("Error: No puedes eliminar una publicación que no te pertenece.")
        else:
            print("Error: Publicación no encontrada.")

    except Exception as e:
        print(f"Error al eliminar la publicación: {e}")
    finally:
        cursor.close()
        connection.close()
 
def ver_publicaciones():
    """
    Muestra las publicaciones almacenadas en la base de datos.
    """
    print("\n=== Publicaciones ===")
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT id_publicacion, id_perfil, contenido, fecha_creacion FROM publicaciones;"
        cursor.execute(query)
        rows = cursor.fetchall()  # Obtiene todas las filas del resultado

        if rows:
            print(f"Se encontraron {len(rows)} publicaciones:")
            for row in rows:
                print(f"ID: {row[0]}, Usuario: {row[1]}, Contenido: {row[2]}, fecha de creacion: {row[3]}")
            
        else:
            print("No hay publicaciones disponibles.")

    except Exception as e:
        print(f"Error al obtener las publicaciones: {e}")
    finally:
        cursor.close()
        connection.close()


def actualizar_publicacion(user_id, post_id, contenido):
    """
    Actualiza el contenido de una publicación si pertenece al usuario autenticado.
    """
    if not user_id:
        print("Error: Usuario no autenticado.")
        return

    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Verificar si la publicación pertenece al usuario autenticado
        query_check = "SELECT id_perfil FROM publicaciones WHERE id_publicacion = %s"
        cursor.execute(query_check, (post_id,))
        result = cursor.fetchone()

        if result:
            post_user_id = result[0]
            if post_user_id == user_id:
                # Actualizar el contenido de la publicación
                query_update = "UPDATE publicaciones SET contenido = %s WHERE id_publicacion = %s"
                cursor.execute(query_update, (contenido, post_id))
                connection.commit()
                print("¡Publicación actualizada exitosamente!")
            else:
                print("Error: No puedes actualizar una publicación que no te pertenece.")
        else:
            print("Error: Publicación no encontrada.")

    except Exception as e:
        print(f"Error al actualizar la publicación: {e}")
    finally:
        cursor.close()
        connection.close()
