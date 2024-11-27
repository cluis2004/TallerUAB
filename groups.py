import mysql.connector
from db_connection import get_connection

def nuevo_grupo(nombre, descripcion, privacidad):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        query = """
        INSERT INTO grupos (nombre, descripcion, privacidad)
        VALUES (%s, %s, %s)
        """
        values = (nombre, descripcion, privacidad)
        
        cursor.execute(query, values)
        connection.commit()
        print("Grupo creado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Ocurrió un error: {err}")
    finally:
        cursor.close()
        connection.close()
