import bcrypt
import mysql.connector
from db_connection import get_connection

def nuevo_perfil(nombre, apellido, fecha_nacimiento, genero, correo, contraseña):
    # Verificar que los campos obligatorios no estén vacíos
    if not all([nombre, apellido, fecha_nacimiento, genero, correo, contraseña]):
        print("Error: Todos los campos son obligatorios. Por favor, rellénelos.")
        return
    
    # Verificar que la contraseña tenga al menos 8 caracteres
    if len(contraseña) < 8:
        print("Error: La contraseña debe tener al menos 8 caracteres.")
        return

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
        print("Se envió un correo de verificación a su dirección de correo electrónico.")
    except mysql.connector.Error as err:
        print(f"Ocurrió un error: {err}")
    finally:
        cursor.close()
        connection.close()
