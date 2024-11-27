# importamos las funciones de los archivos
from profiles import nuevo_perfil
from posts import nueva_publicacion
from posts import eliminar_publicacion
from posts import ver_publicaciones
from posts import actualizar_publicacion
from groups import nuevo_grupo
from login import iniciar_sesion_usuario
from login import actualizar_perfil
from db_connection import get_connection
from comments import nuevo_comentario
from comments import mostrar_comentarios
from comments import eliminar_comentario


current_user_id = None  # Este valor será actualizado cuando inicie sesión

# Función para mostrar el menú principal para el usuario
def mostrar_menu_principal():
    """Registrese o inicie sesión."""
    print("\n=== Menú Principal ===")
    print("1. Iniciar sesión")
    print("2. crear usuario")
    print("0. Salir")
    return input("Selecciona una opción: ")


#funcion para crear comentario
def crear_comentario():
    print("\n=== Crear un Nuevo Comentario ===")
    # Pide el contenido del comentario
    contenido = input("Contenido del comentario: ")
    # Asegúrate de tener el ID de la publicación y del usuario actual
    try:
        id_publicacion = int(input("ID de la publicación a comentar: "))  # Solicitar ID de la publicación
    except ValueError:
        print("Por favor ingresa un ID válido para la publicación.")
        return

    # Suponiendo que 'current_user_id' ya tiene el valor del ID del usuario logueado
    # Llamada a la función para enviar el comentario
    if nuevo_comentario(id_publicacion, contenido, current_user_id):
        print("Comentario enviado exitosamente.")
    else:
        print("Hubo un error al enviar el comentario.")

def ver_comentarios(id_perfil):
    id_publicacion = input("Introduce el ID de la publicación que quieres ver: ")
    mostrar_comentarios(id_publicacion, id_perfil)


def manejar_inicio_de_sesion():
    """Maneja el proceso de inicio de sesión y almacena los user_id del usuario autenticado en la variable global current_user_id."""
    global current_user_id  # Usamos la variable global
    print("\n=== Iniciar Sesión ===")
    correo_electronico = input("Correo electrónico: ")
    contrasena = input("Contraseña: ")
    
    # Suponemos que login_user ahora devuelve el user_id cuando es exitoso
    current_user_id = iniciar_sesion_usuario(correo_electronico, contrasena)
    if current_user_id:
        # Si el inicio de sesión es exitoso, mostramos las opciones
        print(f"¡Inicio de sesión exitoso para el usuario con ID: {current_user_id}!")
        mostrar_menu_opciones()
    else:
        # Si el inicio de sesión falla, mostramos un mensaje de error
        print("Inicio de sesión fallido. Por favor, verifica tus credenciales.")


        
def mostrar_menu_opciones():
    while True:
        print("\n=== Menú opciones ===")
        option = input("1. Crear una nueva publicación\n2. Crear un nuevo grupo\n3. Crear un nuevo comentario\n4. Ver publicaciones\n5. Actualizar perfil\n6. Borrar publicación\n7. Cerrar sesión\n8. Mostrar comentarios\n9. Actualizar Publicacion\n10. Eliminar comentario\nElige una opción: ")
        options = {
            "1": lambda: crear_publicacion(current_user_id),
            "2": nuevo_grupos,
            "3": crear_comentario,
            "4": ver_publicaciones,
            "5": actualizar_perfil,
            "6": lambda: eliminar_publicacion(current_user_id, int(input("Id de la publicación a eliminar: "))),
            "7": manejar_cierre_de_sesion,
            "8": lambda: ver_comentarios(current_user_id),
            "9": lambda: actualizar_publicacion(current_user_id, int(input("ID de la publicacion a actualizar: ")), input("Nuevo contenido: ")),
            "10": lambda: eliminar_comentario(int(input("ID del comentario a eliminar: ")),current_user_id)
        }
        # Llamamos a la función correspondiente a la opción seleccionada
        if option in options:
            options[option]()
            if option == "7":  # Salir del menú si selecciona cerrar sesión
                break
        else:
            print("Opción no válida. Intenta nuevamente.\n")


def manejar_cierre_de_sesion():
    global current_user_id
    print("Cerrando sesión...")
    current_user_id = None  # Restablecemos el usuario actual
    print("Has cerrado sesión exitosamente.")



def crear_perfil():
    print("\n=== Crear un Nuevo Perfil ===")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    opcion = input("seleccione un genero (1. masculino, 2. femenino, 3. Otro): ").strip()
    if opcion == "1":
        genero = "masculino"
    elif opcion == "2":
        genero = "femenino"
    else:
        genero = "otro"
    correo_electronico = input("Correo electrónico: ")
    contrasena = input("Contraseña: ")
    
    nuevo_perfil(nombre, apellido, fecha_nacimiento, genero, correo_electronico, contrasena)


def crear_publicacion(current_user_id):
    print("\n=== Crear una Nueva Publicación ===")
    contenido = input("Contenido de la publicación: ")
    # Usamos el user_id de la sesión actual
    if current_user_id:
        nueva_publicacion(current_user_id, contenido)                             
        
    else:
        print("Debes iniciar sesión primero para crear una publicación.")
        
def nuevo_grupos():
    print("\n=== Crear un Nuevo Grupo ===")
    nombre = input("Nombre del grupo: ")
    descripcion = input("Descripción del grupo: ")
    privacidad = input("Privacidad del grupo (publica/privada/secreta): ")
    
    nuevo_grupo(nombre, descripcion, privacidad)
    print("Grupo creado exitosamente.")

if __name__ == "__main__":
    while True:
        opcion = mostrar_menu_principal()
        if opcion == "1":
            manejar_inicio_de_sesion()
        elif opcion == "2":
            crear_perfil()
        elif opcion == "0":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")