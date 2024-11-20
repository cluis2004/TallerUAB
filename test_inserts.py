from profiles import create_profile
from posts import create_post
from posts import delete_post
from groups import create_group
from login import login_user
from login import update_profile
from db_connection import get_connection

current_user_id = None  # Este valor será actualizado cuando inicie sesión

def menu():
    print("\n=== Menú Principal ===")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("0. Salir")
    return input("Selecciona una opción: ")

def handle_login():
    """Handles the login process, and stores the user_id of the authenticated user in the global variable current_user_id."""
    global current_user_id  # Usamos la variable global
    print("\n=== Iniciar Sesión ===")
    correo_electronico = input("Correo electrónico: ")
    contrasena = input("Contraseña: ")
    
    # Suponemos que login_user ahora devuelve el user_id cuando es exitoso
    current_user_id = login_user(correo_electronico, contrasena)
    if current_user_id:
        # Si el inicio de sesión es exitoso, mostramos las opciones
        print(f"¡Inicio de sesión exitoso para el usuario con ID: {current_user_id}!")
    
        show_menu()
    else:
        # Si el inicio de sesión falla, mostramos un mensaje de error
        print("Inicio de sesión fallido. Por favor, verifica tus credenciales.")


        
def show_menu():
    print("\n=== Menú opciones ===")
    option = input("1. Crear una nueva publicación\n2. Crear un nuevo grupo\n3. Ver publicaciones\n4. Actualizar perfil\n5. Borrar publicación\n6. Cerrar sesión\nElige una opción: ")
    
    options = {
        "1": lambda:handle_create_post(current_user_id),
        "2": handle_create_group,
        "3": handle_view_posts,
        "4": update_profile,
        "5": lambda:delete_post(current_user_id,int(input("Id de la publicación a eliminar: "))),
        "6": handle_logout,  # Implementamos el cierre de sesión
    }
    # Llamamos a la función correspondiente a la opción seleccionada
    options.get(option, lambda: print("Opción no válida. Intenta nuevamente."))()

def handle_logout():
    global current_user_id
    print("Cerrando sesión...")
    current_user_id = None  # Restablecemos el usuario actual
    print("Has cerrado sesión exitosamente.")
    show_menu()  # Volver al menú principal

def handle_view_posts():
    """
    Muestra las publicaciones almacenadas en la base de datos.
    """
    print("\n=== Publicaciones ===")
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT id, id_perfil, contenido FROM publicaciones;"
        cursor.execute(query)
        rows = cursor.fetchall()  # Obtiene todas las filas del resultado

        if rows:
            print(f"Se encontraron {len(rows)} publicaciones:")
            for row in rows:
                print(f"ID: {row[0]}, Usuario: {row[1]}, Contenido: {row[2]}")
            
        else:
            print("No hay publicaciones disponibles.")
        show_menu()

    except Exception as e:
        print(f"Error al obtener las publicaciones: {e}")
    finally:
        cursor.close()
        connection.close()

def handle_create_profile():
    print("\n=== Crear un Nuevo Perfil ===")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    genero = input("Género: ")
    correo_electronico = input("Correo electrónico: ")
    contrasena = input("Contraseña: ")
    
    create_profile(nombre, apellido, fecha_nacimiento, genero, correo_electronico, contrasena)
    print("Perfil creado exitosamente.")

def handle_create_post(current_user_id):

    print("\n=== Crear una Nueva Publicación ===")
    contenido = input("Contenido de la publicación: ")
    
    
    # Usamos el user_id de la sesión
    if current_user_id:
        create_post(current_user_id, contenido)
        show_menu()
    else:
        print("Debes iniciar sesión primero para crear una publicación.")
        
def handle_create_group():
    print("\n=== Crear un Nuevo Grupo ===")
    nombre = input("Nombre del grupo: ")
    descripcion = input("Descripción del grupo: ")
    privacidad = input("Privacidad del grupo (publica/privada/secreta): ")
    
    create_group(nombre, descripcion, privacidad)
    print("Grupo creado exitosamente.")

if __name__ == "__main__":
    while True:
        opcion = menu()
        if opcion == "1":
            handle_login()
        elif opcion == "2":
            handle_create_profile()
        elif opcion == "0":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")
            
            
