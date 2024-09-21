def validar_usuario(nombre_usuario, usuarios):  #  Funcion para validar el nombre del usuario
    if len(nombre_usuario) >= 3:
        if nombre_usuario in usuarios:
            return False  #  El nombre ya existe
        return True  #  Nombre válido y no repetido
    return False  #  Nombre demasiado corto

def comprobarContrasenia(password):  #  Funcion para validar una contraseña segura
    largo = False; mayus = False; numer = False
    if len(password) >= 8: #  Se valida una longitud mínima de 8 caracteres
        largo = True
    for i in range (len(password)):
        if password[i].isupper(): #  Se valida que contenga por lo menos una mayúscula
            mayus = True
        if password[i].isnumeric(): #  Se valida que contenga por lo menos un numero
            numer = True
    if largo and mayus and numer:
        return True
    else:
        return False

#  Funcion para realizar pruebas:

def pruebas():
    validar_usuario(Ana,usuarios)  #  Opcion valida meintras no se repita en el diccionario
    comprobarContrasenia(Ana12345) #  Opcion valida, la funcion devuelve True
    menu1()  #  Menu con opciones de inicio de sesión
    menu2()  #  Menu con opciones para interactuar con el usuario
    
def menu1():  #  Funcion menu para iniciar sesión
    print("--- ENCRIPTACION DE MENSAJES ---")
    print("\n1. Ingresar\n2. Crear usuario y contraseña\n3. Salir")
    
def menu2():  #  Funcion menu para que el usuario interactúe
    print("1. Cifrar un mensaje\n2. Descifrar un mensaje\n3. Generar una llave de cifrado")
    print("4. Validar una llave de cifrado\n5. Cambiar la llave de cifrado\n6. Ver historial de mensajes")
    
def main():
    usuarios = {}  # Se usa un diccionario para almacenar a los usuarios
    while True:
        menu1()
        opcion = int(input("\nIntroduzca una opcion: "))
        match opcion:
        
            case 1:
                if usuarios:  #  Validar que haya usuarios registrados
                    print("Selecciona un usuario para iniciar sesión:")  
                    for i, usuario in enumerate(usuarios.keys(), start = 1):
                        print(f"{i}. {usuario}")  #  Se imprimen los usuarios registrados enumerándolos desde 1.
                
                    seleccion = input("Selecciona un usuario (o '0' para volver): ")
                
                    if seleccion.isdigit() and 0 < int(seleccion) <= len(usuarios):  #  Se valida que sea un numero entero entre 0 y la longitud del diccionario
                        usuario_seleccionado = list(usuarios.keys())[int(seleccion) - 1]
                        contraseña_intentada = input("Ingresa la contraseña: ")
                    
                        if contraseña_intentada == usuarios[usuario_seleccionado]:  #  Se verifica que la contraseña coincida con el usuario
                            print(f"Bienvenido, {usuario_seleccionado}!")
                            print("¿Qué deseas hacer hoy?\n")
                            menu2()  
                            break
                        else:
                            print("Error: Contraseña incorrecta.")
                    elif seleccion == '0':  #  Si se seleccionó cero regresa al menu1
                        continue
                    else:
                        print("Selección no válida.")
                else:
                    print("Primero debe crear un usuario y contraseña!\n")
                
            case 2:
                verificacion = False
                while not verificacion:
                    usuario = input("Ingresa un nombre de usuario: ")
                    verificacion = validar_usuario(usuario, usuarios)  # Se manda a verificar el usuario a la funcion
                    if not verificacion:
                        print("Nombre de usuario invalido!")
                
                verificacion = False
                while not verificacion:
                    cts = input("Introduzca una contrasenia (minimo de 8 caracteres, una mayuscula y un numero): ")
                    verificacion = comprobarContrasenia(cts)  # Se manda a verificar la contraseña a la funcion
                    if not verificacion:
                        print("Contrasenia invalida!")
                usuarios[usuario] = cts  # Se asigna la contraseña al usuario
                print("Usuario y contraseña guardados con éxito!\n")
                
            case 3:
                print("¡Hasta pronto!")
                break
            
main()