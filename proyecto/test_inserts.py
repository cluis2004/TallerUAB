from profiles import create_profile
from posts import create_post
from groups import create_group
from login import login_user

current_user_id = None  # Este valor será actualizado cuando inicie sesión

def menu():
    print("\n=== Menú Principal ===")
    print("1. Iniciar sesión")
    print("2. Crear un nuevo perfil")
    print("3. Crear una nueva publicación")
    print("4. Crear un nuevo grupo")
    print("0. Salir")
    return input("Selecciona una opción: ")

def handle_login():
    global current_user_id  # Usamos la variable global
    print("\n=== Iniciar Sesión ===")
    correo_electronico = input("Correo electrónico: ")
    contrasena = input("Contraseña: ")
    
    # Suponemos que login_user ahora devuelve el user_id cuando es exitoso
    current_user_id = login_user(correo_electronico, contrasena)
    
    if current_user_id:
        print(f"¡Inicio de sesión exitoso para el usuario con ID: {current_user_id}!")
    else:
        print("Error en las credenciales. Intenta nuevamente.")

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

def handle_create_post():
    print("\n=== Crear una Nueva Publicación ===")
    contenido = input("Contenido de la publicación: ")
    
    
    # Usamos el user_id de la sesión
    if current_user_id:
        create_post(current_user_id, contenido)
        print("Publicación creada exitosamente.")
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
        elif opcion == "3":
            handle_create_post()
        elif opcion == "4":
            handle_create_group()
        elif opcion == "0":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")