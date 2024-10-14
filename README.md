# Cifrado de mensajes
CIFRADO DE HILL

### Contexto:

Este proyecto está basado en el cifrado de Hill, en criptografía básica este es un cifrado de sustitución poligráfica basado en el álgebra lineal. Inventado por el matemático estadounidense Lester S. Hill en 1929 y utilizado por el ejército de los Estados Unidos de América en la segunda guerra mundial. 

¿Por qué me llamó la atención?

Pienso que este cifrado es una muy buena aplicación del álgebra lineal y llevarlo a la programación puede ahorrar mucho tiempo a la hora de encriptar o desencriptar mensajes. Además, lleva a la practica el planteamiento de algoritmos de un proceso largo y de cierta manera complejo, ya que hacerlo a mano sería muy tedioso y fácil de cometer errores. También cabe mencionar que este algoritmo nos plantea una reflexión sobre como se puede proteger la información para que personas malintensionadas no hagan mal uso de ella.

### Método de cifrado:

Cada letra del alfabeto inglés está representado por un numero A = 0, B = 1, C = 3, ... , Z = 25 y un espacio representado por '_' asociado al número 26. Para encriptar un mensaje es necesario asignar un numero a cada letra del mensaje y separar por bloques de 3, rellenando si hace falta con espacios. Cada bloque será colocado en la columna de una matriz A de dimensión 3xn donde n es el numero de bloques formados. La matriz usada para la encriptación es la llave de cifrado, y tiene que ser escogida aleatoriamente del conjunto de matrices invertibles n×n (modular 27). Posterior a ello se multiplica la matriz A por la llave de cifrado K obteniendo así una matriz B de 3xn. Finalmente se aplica modulo 27 a cada elemento de B para que coincida con el abecedario, cada columna de esta matriz será puesta en forma lineal sustituyendo cada numero por una letra del alfabeto teniendo así nuestro mensaje cifrado.

### Algoritmo cifrado:

1. Tener un mensaje con letras y espacios
2. Asignar un numero a cada letra y espacio del mensaje de acuerdo al alfabeto ingles  A = 0, B = 1, C = 3, ... , Z = 25, '  ' = 26
3. Separar el mensaje numerico en matrices de 3x1.
4. Formar una matriz A de 3xn con las matrices columna previamente formadas
5. Contar con una matriz K (llave)
6. Validar que la matriz K sea invertible modular(27), para ello se verifica que el determinante sea distinto de cero y que al dividirlo por 3 el residuo no sea cero.
7. Realizar la multiplicacón de K * A para obtener una matriz B
8. Obtener B mod 27
9. Ordenar cada columna de B en forma horizontal y asignar a los numeros las letras correspondientes del vector alfabeto
10. Remplazar cada numero con la letra correspondiente

### Método para decifrar:

Para desencriptar se necesita el mensaje representado por los respectivos numeros colocados en una matriz de 3xn y la llave de cifrado (matriz k). Posterior a ello, se calcula la inversa de k módulo 27 y se multiplica por la matriz del mensaje cifrado. Finalmente, a la matriz resultante se le saca nuevamente módulo 27 y se ordena en una línea sustituyendo los numeros por letras para concluir con el proceso.

### Algoritmo descifrado:

1. Tener el mensaje cifrado y una matriz K (llave)
2. Asignar un numero a cada letra del mensaje respectivamente
3. Separar el mensaje en grupos de 3 y crear una matriz B donde cada columna corresponde a los grupos formados
4. Calcular la inversa de K y sacar modulo 27 a sus elementos
5. Calcular KXB y sacar nuevamente modulo 27 a sus elementos, de ello se obtiene una matriz A
6. Ordenar cada columna de A en forma horizontal y asignar a los numeros las letras correspondientes del vector alfabeto
7. Remplazar cada numero con la letra correspondiente

Para conocer a detalle sobre el método de cifrado y desifrado consulta el siguiente video: https://www.youtube.com/watch?v=ChOhsL-zvBo

### Instrucciones:

1. Instala Thonny en tu computadora o cualquier interprete de Python, video sugerido: https://www.youtube.com/watch?v=np6zQDTPsbE
2. Descarga el archivo CifradoMensajes.py
3. Ejecuta el código

### Uso del programa:

1. Crea un usuario y contraseña
2. Inicia sesión (seleccionar usuario e introducir contraseña)
3. Selecciona una opción en menú

CIFRAR UN MENSAJE:

1. Ingresa un mensaje a cifrar (sólo letras y espacios)
2. Ingresa una matriz llave válida, para ello puedes crear una en la opcion 3 del menu o introducir cualquiera de las siguientes opciones:

K1 = [[-26, -98, 61] , [22, 76, -82] , [11, 70, 71]]
k2 = [[35, -15, -71] , [-95, 85, 29] , [59, -6, -96]]
k3 = [[86, 24, 72] , [76, -5, -30] , [22, 82, 44]]

DECIFRAR UN MENSAJE:

1. Ingresa un mensaje a cifrar (sólo letras y espacios)
2. Ingresa una matriz llave válida, puedes usar el mismo mensaje cifrado con su llave correspondiente o ingresar los ejemplos a continuación.

Copia y pega los siguientes mensajes e introduce manualmente su respectiva llave:

Mensaje1: mbakmivpouhx
Llave: [[35,53,12] , [12,21,5] , [2,4,1]]

Mensjae2: 
