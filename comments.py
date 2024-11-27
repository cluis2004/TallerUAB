import mysql.connector
from mysql.connector import Error
from db_connection import get_connection  # Asumimos que esta función está definida en db_connection.py

def nuevo_comentario(id_publicacion, contenido_comentario, id_perfil):
    if not id_publicacion or not contenido_comentario:
        print("Faltan datos requeridos")
        return False
    # Conectar a la base de datos
    conexion = get_connection()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return False

    try:
        cursor = conexion.cursor()
        consulta = """
            INSERT INTO comentarios (id_publicacion, id_perfil, contenido)
            VALUES (%s, %s, %s)
        """
        valores = (id_publicacion, id_perfil, contenido_comentario)
        cursor.execute(consulta, valores)
        conexion.commit()  # Confirmar los cambios
        print(f"Comentando la publicacion con el ID: {id_publicacion}....")
        return True
    except Error as e:
        print(f"Error al agregar el comentario: {e}")
        return False
    finally:
        cursor.close()
        conexion.close()

def mostrar_comentarios(id_publicacion, id_perfil):
    if not id_publicacion:
        print("Faltan datos requeridos.")
        return False

    # Conectar a la base de datos
    conexion = get_connection()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return False

    try:
        cursor = conexion.cursor()
        consulta = """
            SELECT id_comentario, id_publicacion, id_perfil, contenido, fecha_creacion
            FROM comentarios
            WHERE id_publicacion = %s
        """
        cursor.execute(consulta, (id_publicacion,))
        comentarios = cursor.fetchall()

        if not comentarios:
            print("No se encontraron comentarios para esta publicación.")
            return False

        print("\n=== Comentarios de la publicación ===")
        for comentario in comentarios:
            comentario_id, publicacion_id, perfil_id, contenido, fecha = comentario
            print(f"\nComentario ID: {comentario_id}")
            print(f"ID Publicación: {publicacion_id}")
            print(f"ID Perfil: {perfil_id}")
            print(f"comentario: {contenido}")
            print(f"Fecha de creación: {fecha}")

        return True

    except mysql.connector.Error as e:
        print(f"Error al consultar los comentarios: {e}")
        return False

    finally:
        conexion.close()
def eliminar_comentario(id_comentario, id_perfil):
    # Validación del ID del comentario
    if not id_comentario or not str(id_comentario).isdigit():
        print("Por favor, ingresa un ID de comentario válido (número entero).")
        return False

    # Conectar a la base de datos
    conexion = get_connection()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return False

    try:
        cursor = conexion.cursor()
        # Verificar si el comentario existe y pertenece al perfil
        consulta_verificar = """
            SELECT id_comentario
            FROM comentarios
            WHERE id_comentario = %s AND id_perfil = %s
        """
        cursor.execute(consulta_verificar, (id_comentario, id_perfil))
        comentario = cursor.fetchone()

        if not comentario:
            print("El comentario no existe o no pertenece al usuario actual.")
            return False

        # Eliminar el comentario
        consulta_eliminar = """
            DELETE FROM comentarios
            WHERE id_comentario = %s AND id_perfil = %s
        """
        cursor.execute(consulta_eliminar, (id_comentario, id_perfil))
        conexion.commit()  # Confirmar los cambios

        print(f"Comentario con ID {id_comentario} eliminado exitosamente.")
        return True

    except mysql.connector.Error as e:
        print(f"Error al eliminar el comentario: {e}")
        return False

    finally:
        cursor.close()
        conexion.close()
