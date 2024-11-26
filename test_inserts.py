from profiles import create_profile
from posts import create_post
from groups import create_group
from login import login_user

def menu():
    """Muestra el menú principal del programa."""
    print("\n=== Menú Principal ===")
    print("1. Iniciar sesión")
    print("2. Crear un nuevo perfil")
    print("3. Crear una nueva publicación")
    print("4. Crear un nuevo grupo")
    print("0. Salir")
    return input("Selecciona una opción: ")


def handle_login():
    print("\n=== Iniciar Sesión ===")
    correo_electronico = input("Correo electrónico: ")
    contrasena = input("Contraseña: ")

    if login_user(correo_electronico, contrasena):
        print("¡Inicio de sesión exitoso!")
    else:
<<<<<<< HEAD
        # Si el inicio de sesión falla, mostramos un mensaje de error
        print("Inicio de sesión fallido. Por favor, verifica tus credenciales.")


        
def show_menu():
    
    while True:
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
        if option in options:
            options[option]()
            if option == "6":
                break
        else:
            print("Opción no válida. Intenta nuevamente.\n")

            
def handle_logout():
    global current_user_id
    print("Cerrando sesión...")
    current_user_id = None  # Restablecemos el usuario actual
    print("Has cerrado sesión exitosamente.")


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

    except Exception as e:
        print(f"Error al obtener las publicaciones: {e}")
    finally:
        cursor.close()
        connection.close()
=======
        print("Error en las credenciales. Intenta nuevamente.")
>>>>>>> 45d70d09e6a2ea84ef577732ae4f3ed5fcf0c153

def handle_create_profile():
    print("\n=== Crear un Nuevo Perfil ===")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    genero = input("Género: ")
    correo_electronico = input("Correo electrónico: ")
    contrasena = input("Contraseña: ")
    
    create_profile(nombre, apellido, fecha_nacimiento, genero, correo_electronico, contrasena)


def handle_create_post():
    print("\n=== Crear una Nueva Publicación ===")
    contenido = input("Contenido de la publicación: ")
    
    
<<<<<<< HEAD
    # Usamos el user_id de la sesión
    if current_user_id:
        create_post(current_user_id, contenido)                             
        
    else:
        print("Debes iniciar sesión primero para crear una publicación.")
        
=======
    user_id = 1  # Asegúrate de obtener este id correctamente si es necesario
    create_post(user_id, contenido)
    print("Publicación creada exitosamente.")

>>>>>>> 45d70d09e6a2ea84ef577732ae4f3ed5fcf0c153
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
        elif opcion == "3":
            handle_create_post()
        elif opcion == "4":
            handle_create_group()
        elif opcion == "0":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")
