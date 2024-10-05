import string
import random
from math import gcd

# Se construye una lista con el abecedario inglés en mayusculas más un caracter para el espacio ' '
abecedario = list(string.ascii_uppercase)
abecedario.append(' ')

# Función para ingresar manualmente una matriz 3x3(llave de cifrado)
def ingresar_llave():
    matllave = []
    print("\nIngresa los elementos de la matriz llave:")
    
    for i in range(3):
        fila = []
        for j in range(3):
            valor = int(input(f"Elemento [{i+1},{j+1}]: ")) 
            fila.append(valor)
        matllave.append(fila)
    
    return matllave #Devuelve la matriz 3x3 ingresada por el usuario.
    
# Función que cifra el mensaje usando la matriz llave K
def cifrar_matriz(K, A):
    columnas_A = len(A[0])
    columnas_K = len(K[0])
    
    # Crear la matriz resultado
    resultado = [[0 for _ in range(columnas_A)] for _ in range(3)]
    
    # Multiplica la matriz llave K por la matriz del mensaje A
    for i in range(3):
        for j in range(columnas_A):
            for k in range(3):  
                resultado[i][j] += K[i][k] * A[k][j]
            resultado[i][j] %= 27  # el resultado debe ser mod 27 (para que coincida con el abecedario)
    
    return resultado

# Función que convierte la matriz resultado cifrada en un vector para facilitar la conversión a letras
def vector_mensaje_cifrado(resultado):
    mensaje_cifrado = []
    for i in range(len(resultado[0])):
        for j in range(3):
            mensaje_cifrado.append(resultado[j][i])
    
    return mensaje_cifrado

# Convierte el vector de números cifrados en letras según el abecedario.
def cambiar_a_letras(msj_cifrado):
    mensaje_final = ''
    for numero in msj_cifrado:
        mensaje_final += abecedario[numero]
    return mensaje_final

# Calcula el determinante de una matriz 3x3 usando el metodo de Sarrus
def determinante_3x3(matriz):
    return (matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1]) -
            matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0]) +
            matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]))

# Valida la matriz llave verificando que su determinante sea coprimo con 27.
def validar_llave(K):
    det = determinante_3x3(K)
    if gcd(det,27) == 1 and det != 0: # Calcula el MCD entre el determinante y 27
        return True # Si el resultado es 1 y el determinante es distino de cero significa que K es invertible y modular 27, lo cual es valido                
    else:
        return False

#Genera una matriz llave 3x3 aleatoria que sea válida
def crear_llave():
    while True:
        K = [[random.randint(-100, 100) for _ in range(3)] for _ in range(3)] # Los elementos de la matriz llave serán en un rango entre -100 y 100
        if validar_llave(K):
            return K

# Convierte el mensaje de texto en un vector de números según los índices del abecedario
def vector_mensaje(mensaje):
    mns = []
    for letra in mensaje:
        indice = abecedario.index(letra)
        mns.append(indice)
    while len(mns) % 3 != 0:
            mns.append(26)
            
    return mns

# Convierte el vector de números del mensaje en una matriz de 3 filas
def matriz_mensaje(ML):
    tamano = (len(ML)) // 3
    M3xn = [[0] * tamano for _ in range(3)]
    
    k = 0
    for i in range(tamano):
        for j in range(3):
            M3xn[j][i] = ML[k]
            k += 1

    return M3xn

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

mensaje_usuario = "Hola mundo" # mensaje de prueba, se debe ingresar manualmente la matriz llave: [[35,53,12],[12,21,5],[2,4,1]] para que sea valida
mensaje = mensaje_usuario.upper()

def pruebas():
    validar_usuario(Ana,usuarios)  #  Opcion valida meintras no se repita en el diccionario
    comprobarContrasenia(Ana12345) #  Opcion valida, la funcion devuelve True
    menu1()  #  Menu con opciones de inicio de sesión
    menu2()  #  Menu con opciones para interactuar con el usuario
    K = ingresar_llave()
    print(validar_llave(K))
    MSJ = matriz_mensaje(vector_mensaje(mensaje))
    res = cifrar_matriz(K, MSJ)
    men = vector_mensaje_cifrado(res)
    print(cambiar_a_letras(men))
    
def menu1():  #  Funcion menu para iniciar sesión
    print("--- ENCRIPTACION DE MENSAJES ---")
    print("\n1. Ingresar\n2. Crear usuario y contraseña\n3. Salir")
    
def menu2():  #  Funcion menu para que el usuario interactúe
    print("1. Cifrar un mensaje\n2. Descifrar un mensaje\n3. Generar una llave de cifrado")
    print("4. Validar una llave de cifrado\n5. Ver historial de mensajes\n6. Cerrar sesion")
    
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
                            print(f"\nBienvenid@, {usuario_seleccionado}!")
                            print("¿Qué deseas hacer hoy?\n")
                            while True:
                                menu2()
                                op = int(input("\nSelecciona una opcion: "))
                                match op:
                                    case 1:
                                        print("¡Opcion no disponible por el momento!\n")
                                    case 2:
                                        print("¡Opcion no disponible por el momento!\n")
                                    case 3:
                                        print("¡Opcion no disponible por el momento!\n")
                                    case 4:
                                        print("¡Opcion no disponible por el momento!\n")
                                    case 5:
                                        print("¡Opcion no disponible por el momento!\n")
                                    case 6:
                                        print(f"Sesion cerrada con exito\n!Hasta pronto {usuario_seleccionado}!\n")
                                        break
                                    case _:
                                        print("!Opcion no valida!\n")
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
            
            case _:
                print("¡Opcion inválida!\n")        
main()
