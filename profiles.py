import bcrypt
import mysql.connector
from db_connection import get_connection

def create_profile(nombre, apellido, fecha_nacimiento, genero, correo, contraseña):
    try:
        # Encriptar la contraseña con bcrypt
        hashed_password = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())
        
        connection = get_connection()
        cursor = connection.cursor()
        
        query = """
        INSERT INTO perfiles (nombre, apellido, fecha_nacimiento, genero, correo_electronico, contrasena)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (nombre, apellido, fecha_nacimiento, genero, correo, hashed_password)
        
        cursor.execute(query, values)
        connection.commit()
        print("Perfil creado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Ocurrió un error: {err}")
    finally:
        cursor.close()
        connection.close()
