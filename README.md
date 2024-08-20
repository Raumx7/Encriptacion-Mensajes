# Encriptación de mensajes
CIFRADO DE HILL

Contexto:

Este proyecto está basado en el cifrado de Hill, en criptografía básica este es un cifrado de sustitución poligráfica basado en el álgebra lineal. Inventado por el matemático estadounidense Lester S. Hill en 1929 y utilizado por el ejército de los Estados Unidos de América en la segunda guerra mundial. 

¿Por qué me llamó la atención?

Pienso que este cifrado es una muy buena aplicación del álgebra lineal y llevarlo a la programación puede ahorrar mucho tiempo a la hora de encriptar o desencriptar mensajes. Además, lleva a la practica el planteamiento de algoritmos de un proceso largo y de cierta manera complejo, ya que hacerlo a mano sería muy tedioso y fácil de cometer errores. También cabe mencionar que este algoritmo nos plantea una reflexión sobre como se puede proteger la información para que personas malintensionadas no hagan mal uso de ella.

Método de cifrado:

Cada letra del alfabeto inglés está representado por un numero A = 0, B = 1, C = 3, ... , Z = 25 y un espacio representado por '_' asociado al número 26. Para encriptar un mensaje, cada bloque de n letras (considerados como un vector) está multiplicado por una matriz. La matriz usada para la encriptación es la llave de cifrado, y tiene que ser escogida aleatoriamente del conjunto de matrices invertibles n×n (modular 26). El cifrado puede naturalmente, ser adaptado a un alfabeto representado con cualquier orden numerico y/o cambiando el número (modular 26) siempre y cuando la matriz n×n (modular x) sea invertible. Posterior a ello se multiplica cada vector del mensaje ordenado en 3 filas por la matriz 3x3, así obteniendo una nueva matriz B a la que sacaremos módulo 27. Después sólo queda acomodar las columnas de la matriz en una linea y sustituir los numeros por sus respectivas letras.

Método para decifrar:

Para desencriptar se necesita el mensaje representado por los respectivos numeros colocados en una matriz de 3xn y la llave de cifrado (matriz k). Posterior a ello, se calcula la inversa de k módulo 27 y se multiplica por la matriz del mensaje cifrado. Finalmente, a la matriz resultante se le saca nuevamente módulo 27 y se ordena en una línea sustituyendo los numeros por letras para concluir con el proceso.

Algoritmo cifrado:

Entradas:

1. Mensaje
2. K """ Matriz llave 3x3 modular (26) """

Proceso:

1. Convertir el string con n caracteres en Mensaje a mayúsculas y sustituir espacios por '_'
2. Asignar un numero a cada letra y espacio de Mensaje de acuerdo al vector alfabeto
3. Separar Mensaje en arreglos unidimensionales de 3 componentes cada uno y rellenar con espacios ('_' = 26) las componentes faltantes
4. Formar una matriz A de 3xn con los arreglos previos
5. Ingresar o inicializar el proceso para construir una matriz K (llave)
6. Validar que la matriz K sea invertible modular(26), para ello se verifica que el determinante sea distinto de cero y que al dividirlo por 2 y 13 el residuo no sea cero.
7. Realizar la multiplicacón de K * A para obtener una matriz B
8. Obtener B mod 27
9. Ordenar cada columna de B en forma horizontal y asignar a los numeros las letras correspondientes del vector alfabeto

Salidas:

1. caracteres del vector alfabeto

Algoritmo descifrado:

Entradas:

1. Mensaje encriptado
2. K """ Llave de cifrado """
