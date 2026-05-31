# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencias_letras(texto):
    texto = texto.replace(" ", "")
    frecuencias = {}                         # Creamos un diccionario vacio nombrado como frecuencias

    for letra in texto:                      # Se recorren todas las lentras en el texto.        
        if letra in frecuencias:             # Si la letra existe y se repite se agrega al contador de frecuencias.
            frecuencias[letra] += 1          
        else:                                # Si la letra aparece por primera vez y no se repite, se añade a 1
            frecuencias[letra] = 1           
            
    return frecuencias            

# Ejemplo:

texto = "Python is super"
print(frecuencias_letras(texto))

# Output: {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, 'i': 1, 's': 2, 'u': 1, 'e': 1, 'r': 1}

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def duplicar(x):
    return x * 2

# Ejemplo:

numeros = [1, 2, 3, 4, 5]

numeros_dobles = list(map(duplicar, numeros))

print(numeros_dobles)

# Output: [2, 4, 6, 8, 10]

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.


def lista_original(lista_palabras, palabra_objetivo):         # Fijamos los parametros, lista_palabras y palabra_objetivo
    lista_nueva = []                                          # Creamos un variable lista_nueva como lista vacia
    for palabra in lista_palabras:                            # Se recorre en la lista de palabras las palabras que cumplan la condición de palabra_objetivo y la añadimos a la lista_nueva vacia.
        if palabra_objetivo.lower() in palabra.lower():       # Usamos la función lower() para no discriminar entre mayúsculas y minúsculas.
           lista_nueva.append(palabra)
    return lista_nueva

# Ejemplo:

palabras = ["Dispuesto", "DISPONIBLE", "Indispensable", "DISturbio", "Destacado"]
palabra_objetivo = "Dis"

print(lista_original(palabras, palabra_objetivo))

# Output: ['Dispuesto', 'DISPONIBLE', 'Indispensable', 'DISturbio']

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def restar(x,y):
    return x - y

def diferencia_listas(lista1, lista2):
    return list(map(restar, lista1, lista2))

# Ejemplo

lista1 = [32, 76, 25]
lista2 = [13, 7, 10]

print(diferencia_listas(lista1, lista2))

# Output: [19, 69, 15]

# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5.La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def evaluar_notas(lista_numeros, nota_aprobado=5):
    media = sum(lista_numeros) / len(lista_numeros)

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return (media, estado)

# Ejemplo

notas = [6, 7, 5, 8]

resultado = evaluar_notas(notas)
print(resultado)

# Resultado: (6.5, 'aprobado')

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Ejemplo

print(factorial(5))  

# Output: 120

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tupla_a_string(tupla):
    return tupla

def tuplas_a_strings(lista_tuplas):
    return list(map(tupla_a_string, lista_tuplas))

# Ejemplo:

lista = [('1'), ("Star Wars"), ('33'), ("Python")]

resultado = tuplas_a_strings(lista)

print(resultado)

# Output: ['1', 'Star Wars', '33', 'Python']

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. 
# Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

try:
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    resultado = a / b
except ValueError:
    print("Debe ingresar un número válido")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
else:
    print("El resultado de la división es:", round(resultado, 2))

# Ejemplo: input 5 / 7
# Output: El resultado de la división es: 0.71

# Ejemplo: input A
# Output: Debe ingresar un número válido

# Ejemplo: input 3 / 0
# Output: No se puede dividir entre cero

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. 
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. 
# Usa la función filter()

def mascota_permitida(mascota):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return mascota not in prohibidas

def filtrar_mascotas(lista_mascotas):
    return list(filter(mascota_permitida, lista_mascotas))

# Ejemplo:

mascotas = ["Perro", "Gato", "Mapache", "Tortuga", "Oso", "Canario"]

resultado = filtrar_mascotas(mascotas)

print(resultado)

# Output: ['Perro', 'Gato', 'Tortuga', 'Canario']

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente

class Lista_Vacia(Exception):                                                     # Definimos una clase de excepción personalizada llamada Lista_Vacia que hereda de la clase base Exception. Esta clase se utilizará para indicar que la lista está vacía cuando se intente calcular el promedio.
    pass                                                                          # Ponemos pass para indicar que se implementa ninguna función adicional en esta clase de excepción personalizada.

def calcular_promedio(numeros):                                                    # Definimos una función llamada calcular_promedio que recibe una lista de números como argumento.
    if not numeros:                                                                    # Verificamos si la lista de números está vacía utilizando la condición if not numeros. Si la lista está vacía, se lanza una excepción personalizada Lista_Vacia con un mensaje que indica que no se puede calcular el promedio.
        raise Lista_Vacia("La lista está vacía, no se puede calcular el promedio.")
    return sum(numeros) / len(numeros)                                                 # Si la lista no está vacía, se calcula el promedio sumando todos los números en la lista utilizando la función sum() y dividiendo por la cantidad de números en la lista utilizando len(). El resultado se devuelve como el promedio de los números en la lista.

# Ejemplo:  

try:                                                                            # Utilizamos try para intentar calcular el promedio de una lista de números. Si la lista está vacía, se lanzará la excepción personalizada Lista_Vacia y se manejará en el bloque except.
    lista = [10, 58, 47, 8]
    promedio = calcular_promedio(lista)
    print("El promedio es:", round(promedio, 2))
except Lista_Vacia:
    print("La lista está vacía, no se puede calcular el promedio.")

  # Output: 30.75 
  # Output Lista Vacia: La lista está vacía, no se puede calcular el promedio.

  # 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

try:
    edad = float(input("Ingrese su edad: "))
    if edad < 0 or edad > 120:
        raise ValueError("Ingrese una edad válida (entre 0-120)")
except ValueError:
    print("Ingrese una edad válida (entre 0-120)")
else:
    print("Su edad es:", round(edad, 2))

# Ejemplo: Input 25
# Output: 25.0

# Ejemplo: Input 127
# Output:  Ingrese una edad válida (entre 0-120)

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras(frase):
    palabras = frase.split()

    return list(map(len, palabras))

# Ejemplo:

frase = "Hoy es un buen dia para entrenar"
print(longitud_palabras(frase))

# Output: [3, 2, 2, 4, 3, 4, 8]

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas.Usa la función map()

def convertir(letra):                         # Creamos una función para convertir una tupla de letras de minucsulas a mayusculas y viceversa.
    return letra.upper(), letra.lower()

def mayusc_minusc(caracteres):                # Creamos otra función para un conjunto de caracteres
    unicos = []                               # Creamos el variable unicos con lista vacia
    for c in caracteres:                      # Recorremos caracter a caracter con el bucle for el conjuto de caracteres
        if c.lower() not in unicos:           # Si el caracter convertido a minusculas no esta en la lista, se añade. Si no, no.
            unicos.append(c.lower())          # Al final del bucle se insertan en la lista unicos los caracteres únicos y en minusculas
    return list(map(convertir, unicos))       # Mediante map se aplica la funcion convertir a cada elemento de unicos y se converte a lista de tuplas. 

# Ejemplo: "Alameda"

letras = "Alameda"
print(mayusc_minusc(letras))

# Output: [('A', 'a'), ('L', 'l'), ('M', 'm'), ('E', 'e'), ('D', 'd')]

# 14. Crea una función que retorne las palabras de una lista de palabras que contengan una letra en especifico. Usa la función filter()

def lista_palabras(palabra):
    letra = 'y'
    return letra.lower() in palabra.lower()

def filtrar_palabras(lista):
    return list(filter(lista_palabras, lista))

# Ejemplo:

lista =  "Maracuya", "PAPAYA", "Banana", "Coco"
print(filtrar_palabras(lista))

# Output: ['Maracuya', 'PAPAYA']

# 15. Crea una función lambda que sume 3 a cada número de una lista dada

# 1.- Definimos la función lambda que recorre los elementos números en una lista de numeros y les suma 3 a cada uno. 
funcion_lambda_sum3 = lambda lista_numeros: [elemento + 3 for elemento in lista_numeros]

# 2.- Creamos una lista de números de prueba
lista_num_prueba = [34, 39, 12, 15]

# 3.- Llamamos a nuestra función lambda con la lista de números de prueba y almacenamos el resultado
lista_numeros_sum3 = funcion_lambda_sum3(lista_num_prueba)

print(lista_numeros_sum3)

# Output: [37, 42, 15, 18]

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def palabra_mas_larga(texto, n):
    return list(filter(lambda palabra: len(palabra) > n, texto.split()))

def filtrar_palabras(lista, n):
    return list(filter(lambda palabra: len(palabra) > n, lista))

# Ejemplo:

lista = ("Mercedes", "Audi", "TOYOTA", "SEat")
print(filtrar_palabras(lista, 4))

# Output: ['Mercedes', 'TOYOTA']

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def combinar(acumulado, d):                           # se define la función combinar con parametros acumulado y d (digito)
    return acumulado * 10 + d                         # se retorna el acumulado que se multiplica por 10 y se le suma el d

def lista_a_numero(digitos):                          # se define una funnción que pase una lista de números con parametro digitos
    return reduce(combinar, digitos)                  # mediante reduce se combinan los digitos uno a uno con la prinera función

print(lista_a_numero([5, 7, 2]))

# Output: 572

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. 
# Usa la función filter()

estudiantes = [
      {"Nombre": "Ana", "edad": 19, "calificacion": 89},           # definimos un variable con lista de diccionarios nombre, edad, calificación.
      {"Nombre": "Pedro", "edad": 21, "calificacion": 91},
      {"Nombre": "Lola", "edad": 23, "calificacion": 95},
      {"Nombre": "Luis", "edad": 22, "calificacion": 88}
]

def calificacion_alta(estudiante):                                 # definimos la función para destacar los estudiantes con calificacion igual o mayor de 90
    return estudiante["calificacion"] >= 90

estudiantes_destacados = list(filter(calificacion_alta, estudiantes))  # filtramos en la función los estudinantes que cumplen el requisito de retorno
print(estudiantes_destacados)

# Output: [{'Nombre': 'Pedro', 'edad': 21, 'calificacion': 91}, {'Nombre': 'Lola', 'edad': 23, 'calificacion': 95}]

# 19 Crea una función lambda que filtre los números impares de una lista dada

def filtrar_impares(lista):
    return list(filter(lambda x: x % 2 != 0, lista))

# Ejemplo:

lista = [1, 2, 4, 5, 6, 7, 5]
print(filtrar_impares(lista))

# Output: [1, 5, 7, 5]

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

def es_entero(elemento):
    return isinstance(elemento, int)

def lista_int(lista_mixta):
    return list(filter(es_entero, lista_mixta))

# Ejemplo:
lista_mixta = [11, "Hola", 33, "Nuevo"]
resultado = lista_int(lista_mixta)

print(resultado)
# Output: [11, 33]

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

elevar_cubo = lambda n: n ** 3

# Ejemplo
print(elevar_cubo(3))

# Output: 27

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() 

from functools import reduce

def sumar(a, b):
    return a + b

def total_numero(producto):
    return reduce(sumar, producto)

# Ejemplo:
productos = [1, 2, 3, 5, 6, 7, 9]
print(total_numero(productos))

# Output: 33

# 23. Concatena una lista de palabras.Usa la función reduce().

from functools import reduce

def concatenar(a, b):
    return a + " " + b

def lista_reducida(palabras):
    return reduce(concatenar, palabras)
# Ejemplo

palabras = ["Python", "JAVAscript", "CSS", "Robin Hood"]
print(lista_reducida(palabras))

# Output: "Python JAVAscript CSS Robin Hood"

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .    

from functools import reduce

def diferencia(lista):
    return reduce(lambda a, b: a - b, lista)

# Ejemplo:

numeros = [10, 2, 3, 4, 1]
print(diferencia(numeros))

# Output: 0

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.


def contar_caracteres(texto):
    return len(texto)

# Ejemplo:
texto = "Hoy es un día bonito"
print(contar_caracteres(texto))

# Output: 20

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

funcion_lambda = lambda x, y: x % y

# Ejemplo:

print(funcion_lambda(10, 3))  

# Output: 1

# 27. Crea una función que calcule el promedio de una lista de números.

def promedio(lista):
    return sum(lista) / len(lista)

# Ejemplo:

lista_numeros = [1, 3, 4, 3, 6, 33]
print (round(promedio(lista_numeros), 2))

# Output: 8.33

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):                   # Definimos una función llamada primer_duplicado que recibe una lista como argumento.
    vistos = set()                             # Creamos un conjunto vacío llamado vistos para almacenar los elementos de una lista.
    for elemento in lista:                     # Se recorre cada elemento en la lista utilizando un bucle for.
        if elemento in vistos:                 # Verificamos si el elemento actual ya ha sido visto anteriormente utilizando la condición if elemento in vistos. 
            return elemento                    # Si el elemento ya ha sido visto, se devuelve ese elemento como el primer duplicado encontrado.
        vistos.add(elemento)                   # Si el elemento no ha sido visto antes, se agrega al set de vistos utilizando el método add(). 
    return None                                # Si no hay duplicados

# Ejemplo:
numeros = [3, 4, 5, 6, 3, 7, 8]
print(primer_duplicado(numeros))

# Output: 3

# 29. Crea una función que convierta una variable en una cadena de texto 
# y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def enmascarar(variable):                                                     # Definimos la función enmascarar que toma una variable como argumento.
    variable_str = str(variable)                                              # Convertimos la variable a una cadena de texto y la almacenamos en la variable variable_str.
    if len(variable_str) <= 4:                                                # Verificamos si la longitud de variable_str es menor o igual a 4.
       return variable_str                                                    # Si la longitud es menor o igual a 4, devolvemos variable_str sin enmascarar.
    
    else:                                                                     # Si la longitud es mayor a 4, enmascaramos todos los caracteres excepto los últimos cuatro.
       return '#' * (len(variable_str) - 4) + variable_str[-4:]               # Devolvemos una cadena de caracteres '#' repetida y concatenada con los últimos cuatro caracteres de variable_str.    

# Ejemplo:

digitos = 21212221251245
print(enmascarar(digitos))

# Output: ############1245

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1, palabra2):                        
    return sorted(palabra1) == sorted(palabra2)
# Ejemplo:
print(son_anagramas("amor", "roma"))  

# Output: True

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. 
# Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.


def buscar_nombre():                                                         # Define la función buscar_nombre que no recibe parámetros
    lista_nombres = input("Ingrese una lista de nombres: ").split(",")       # Separa los nombres por comas y crea una lista
    nombre_buscar = input("Ingrese un nombre para buscar en la lista: ")     # Solicita el nombre a buscar
    
    if nombre_buscar.lower() in [n.lower() for n in lista_nombres]:          # Compara el nombre a buscar con los nombres de la lista, ignorando mayúsculas/minúsculas
        return nombre_buscar                                                 # Si se encuentra, devuelve el nombre encontrado
    else:                                                                    # Si no se encuentra, lanza una excepción con un mensaje de error
        raise ValueError(f"{nombre_buscar} no se encuentra en la lista")     # El mensaje de error incluye el nombre que se intentó buscar


try:                                                                         # Intenta ejecutar la función buscar_nombre y captura el resultado
    nombre = buscar_nombre()                                                 # Si se encuentra el nombre, se almacena en la variable 'nombre'
    print(f"El nombre encontrado es {nombre}")                               # Imprime un mensaje indicando el nombre encontrado
except ValueError as e:                                                      # Si se lanza una excepción de tipo ValueError, captura el error en la variable 'e'
    print(e)                                                                 # Imprime el mensaje de error capturado, que indica que el nombre no se encuentra en la lista

# Ejemplo:
# Ingrese una lista de nombres: Ana, Pedro, Marta, Luis
# Ingrese un nombre para buscar en la lista: Pedro

# Output: El nombre encontrado es Pedro

# 32. Crea una función que tome un nombre completo y una lista de empleados, 
# busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, 
# devuelve un mensaje indicando que la persona no trabaja aquí.


def buscar_empleado(nombre_empleado, lista_empleados):                           # Definimos una función con dos parámetros: el nombre del empleado a buscar y la lista de empleados.
    for empleado in lista_empleados:                                             # Se recorre cada empleado en la lista de empleados.
        if empleado["nombre"] == nombre_empleado:                                # Si el nombre del empleado coincide con el nombre que estamos buscando,
           return empleado["posicion"]                                           # se devuelve el puesto del empleado.
        
    return f"{nombre_empleado} no trabaja aquí"                                  # Si el bucle termina sin encontrar el empleado, se devuelve un mensaje indicando que la persona no trabaja aquí.
           
empleados = [{"nombre": "Marta Gomez", "posicion": "Analista"},                  # Creamos una lista de empleados, donde cada empleado es un diccionario con su nombre y posición.
             {"nombre": "Roberto Cuco", "posicion": "Comercial"},
             {"nombre": "Nuria Beltran", "posicion": "Contable"}
]

# Ejemplo:

print(buscar_empleado("Roberto Cuco", empleados))                              # Buscamos el nombre del empleado en la lista de empleados y mostramos su posición si se encuentra, o un mensaje si no se encuentra.

# Output: Comercial

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

a = [1, 3, 4, 5, 7]
b = [2, 5, 5, 7, 5]

print(sumar_listas(a, b))

# Output: [3, 8, 9, 12, 12]

# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. 
# Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . 
# El objetivo es implementar estos métodos para manipular la estructura del árbol.
#  Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
# 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, 
# el número de ramas y las longitudes de las  mismas.

# Caso de uso: 
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.


                                                
class Arbol:                                                       # Creamos la clase arbol
    def __init__(self):                                            # 1. Inicializamos el arbol con un tronco de longitud 1 y una lista vacía de ramas
        self.tronco = 1                                            #    definimos la longitud del tronco inicializada en 1
        self.ramas = []                                            #    creamos una lista vacía de ramas

    def crecer_tronco(self):                                       # 2. Definimos el método crecer_tronco para aumentar la longitud del tronco en una unidad
        self.tronco += 1                                           #   metodo para agregar una nueva rama de longitud 1 a la lista de ramas
    
    def nueva_rama(self):                                          # 3. Definimos el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas
        self.ramas.append(1)                                       #    metodo para aumentar en una unidad la longitud de todas las ramas existentes

    def crecer_ramas(self):                                        # 4. Definimos el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes
        self.ramas = [r + 1 for r in self.ramas]                   #    metodo utilizado con bucle for en list comprehension. 

    def quitar_rama(self, posicion):                               # 5. Definimos el método quitar_rama para eliminar una rama en una posición específica
        if 0 <= posicion < len(self.ramas):                        #    verificamos que la posición sea válida antes de eliminar la rama
            self.ramas.pop(posicion)                               #    eliminamos la rama en la posición especificada
        else:                                                      #    si la posición es inválida, mostramos un mensaje de error
            print("Posición inválida")                        

    def info_arbol(self):                                          # 6. Definimos el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas
        return {                                                   #    devolvemos un diccionario con la información del árbol
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

# Ejemplo:


arbol = Arbol()                                                    # 1. Crear un árbol

arbol.crecer_tronco()                                              # 2. Hacer crecer el tronco una unidad

arbol.nueva_rama()                                                 # 3. Añadir una nueva rama

arbol.crecer_ramas()                                               # 4. Hacer crecer todas las ramas una unidad

# 5. Añadir dos nuevas ramas
arbol.nueva_rama()                                                 # 5. Añadir dos nuevas ramas
arbol.nueva_rama()

arbol.quitar_rama(2)                                               # 6. Retirar la rama situada en la posición 2

print(arbol.info_arbol())                                          # 7. Obtener información del árbol

# Output: {'longitud_tronco': 2, 'numero_ramas': 2, 'longitudes_ramas': [2, 1]}


# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y 
# agregar dinero al saldo.
# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True o False .
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario

# Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
# 2. Agregar 20 unidades de saldo de "Bob".
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# 4. Retirar 50 unidades de saldo a "Alicia"

class UsuarioBanco:                                                           # Creamos la clase UsuarioBanco
    def __init__(self, nombre, saldo, cuenta_corriente):                      # 1. Inicializamos el usuario con su nombre, saldo y si tiene o no cuenta corriente mediante Treu o False .
        self.nombre = nombre                                                  # metodo constructor que recibe el nombre, saldo y cuenta_corriente como parámetros y los asigna a los atributos de la clase.
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente   

    def retirar_dinero(self, cantidad):                                       # 2. Implementamos el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
        if cantidad <= 0:                                                     # Si la cantidad a retirar es menor o igual a cero, se lanza un error indicando que la cantidad debe ser mayor que cero.
            raise ValueError("La cantidad debe ser mayor que cero")

        if cantidad > self.saldo:                                             # Si la cantidad a retirar es mayor que el saldo disponible, se lanza un error indicando que el saldo es insuficiente para retirar dinero.
            raise ValueError("Saldo insuficiente para retirar dinero")
        
        self.saldo -= cantidad                                                # se resta la cantidad del saldo del usuario, retirando el dinero solicitado.

    def transferir_dinero(self, otro_usuario, cantidad):                     # 3. Implementamos el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
        if cantidad <= 0:                                                    # Si la cantidad a transferir es menor o igual a cero, se lanza un error indicando que la cantidad debe ser mayor que cero.
            raise ValueError("La cantidad debe ser mayor que cero")

        if cantidad > otro_usuario.saldo:                                    # Si la cantidad a transferir es mayor que el saldo del otro usuario, se lanza un error indicando que el otro usuario no tiene suficiente saldo para transferir.
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir")

        otro_usuario.saldo -= cantidad                                       # El otro usuario envía dinero al usuario actual, restando la cantidad del saldo del otro usuario y sumándola al saldo del usuario actual.
        self.saldo += cantidad                                               # El usuario actual recibe el dinero, sumando la cantidad al saldo del usuario actual.

    def agregar_dinero(self, cantidad):                                      # 4. Implementamos el método agregar_dinero para agregar dinero al saldo del usuario.
        if cantidad <= 0:                                                    # Si la cantidad a agregar es menor o igual a cero, se lanza un error indicando que la cantidad debe ser mayor que cero.
            raise ValueError("La cantidad debe ser mayor que cero")

        self.saldo += cantidad                                               # Se agrega la cantidad al saldo del usuario.

    
    def info_usuario(self):                                                  # Método para mostrar la información del usuario en formato de diccionario.
        return {
            "nombre": self.nombre,
            "saldo": self.saldo,
            "cuenta_corriente": self.cuenta_corriente
        }


# Ejemplo:

alicia = UsuarioBanco("Alicia", 100, True)                                   # 1. Crear dos usuarios
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(40)                                                       # 2. Agregar 20 unidades al saldo de Bob

alicia.transferir_dinero(bob, 80)                                            # 3. Hacer una transferencia de 80 unidades desde Bob a Alicia

alicia.retirar_dinero(50)                                                    # 4. Retirar 50 unidades de saldo a Alicia


print(alicia.info_usuario())
print(bob.info_usuario())

# Output:
# {'nombre': 'Alicia', 'saldo': 130, 'cuenta_corriente': True}
# {'nombre': 'Bob', 'saldo': 10, 'cuenta_corriente': True}

# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: reemplazar_palabras , 
# procesar_texto .contar_palabras , eliminar_palabra . 
# Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función 
# Código a seguir:

# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tieneque devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.

# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto. 

def contar_palabras(texto):                                             # 1. Creamos la función contar_palabras para contar el número de veces que aparece cada palabra en el texto para devolver un diccionario. 
    palabras = texto.split()                                            # Se divide el texto en palabras utilizando el método split(), lo que genera una lista de palabras.
    conteo = {}                                                         # Se crea un diccionario vacío llamado conteo para almacenar el número de veces que aparece cada palabra.
    for palabra in palabras:                                            # Se recorre cada palabra en la lista de palabras.
        if palabra in conteo:                                           # Si la palabra ya está en el diccionario conteo, se incrementa su contador en 1.
            conteo[palabra] += 1
        else:                                                           # Si la palabra no está en el diccionario conteo, se agrega al diccionario con un contador inicial de 1.
            conteo[palabra] = 1
    return conteo                                                       # Se devuelve el diccionario conteo con el número de veces que aparece cada palabra en el texto.

def reemplazar_palabras(texto, palabra_original, palabra_nueva):        # 2. Creamos la función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva para devolver el texto con el remplazo de palabras. 
    return texto.replace(palabra_original, palabra_nueva)               # Con el método replace() se reemplazan todas las apariciones de palabra_original por palabra_nueva en el texto, y se devuelve el texto modificado.

def eliminar_palabra(texto, palabra_a_eliminar):                        # 3. Creamos la función eliminar_palabra para eliminar una palabra del texto y para devolver el texto con la palabra eliminada.
    return texto.replace(palabra_a_eliminar, "")                        # Con el método replace() se reemplazan todas las apariciones de palabra_a_eliminar por una cadena vacía "", lo que elimina la palabra del texto, y se devuelve el texto modificado.

def procesar_texto(texto, opcion, *args):                               # 4. Creamos la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Para la opción 'reemplazar' se necesitan dos argumentos: palabra_original y palabra_nueva")
        return reemplazar_palabras(texto, args[0], args[1])            # Si la opción es "reemplazar", se verifica que se hayan proporcionado exactamente dos argumentos (palabra_original y palabra_nueva). 
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Para la opción 'eliminar' se necesita un argumento: palabra_a_eliminar")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Las opciones válidas son: 'contar', 'reemplazar', 'eliminar'")
    
# Ejemplo de caso de uso:

texto = "Hola mundo, hola a todos. El mundo es grande."                   # 1. Definimos una variable texto con una cadena de texto para probar la función procesar_texto con las diferentes opciones.
print(procesar_texto(texto, "contar"))                                    # 2. Contamos el número de veces que aparece cada palabra en el texto y mostramos el resultado por terminal.
print(procesar_texto(texto, "reemplazar", "mundo", "universo"))           # 3. Reemplazamos la palabra "mundo" por "universo" en el texto y mostramos el resultado por terminal.
print(procesar_texto(texto, "eliminar", "hola"))                          # 4. Eliminamos la palabra "hola" del texto y mostramos el resultado por terminal.

# Output:
# {'Hola': 1, 'mundo,': 1, 'hola': 1, 'a': 1, 'todos.': 1, 'El': 1, 'mundo': 1, 'es': 1, 'grande.': 1}
# Hola universo, hola a todos. El universo es grande.
# Hola mundo,  a todos. El mundo es grande.

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

hora = int(input("Ingrese la hora (0-24): "))

if hora < 0 or hora > 24:
    print("Hora no válida")
elif hora >= 0 and hora <= 12:
    print("Es de día")
elif hora >= 12 and hora <= 18:
    print("Es tarde")
else:
    print("Es de noche")

# Ejemplo:

# Input: 6 
# Output: Es de día
# Input: 18 
# Output: Es tarde
# Input: 20 
# Output: Es de noche
# Input: 25
# Output: Hora no válida

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
# Las reglas de calificación son:
# - 0  - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente 


def calificacion_texto(nota):
    if nota < 0 or nota > 100:
        return "Calificación no válida"
    elif nota <= 69:
        return "insuficiente"
    elif nota <= 79:
        return "bien"
    elif nota <= 89:
        return "muy bien"
    else:
        return "excelente"

# Ejemplo:

nota = 67
resultado = print(calificacion_texto(nota))

# Output: insuficiente

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectángulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

def calcular_area(figura, datos):
    figura = figura.lower()

    if figura == "rectángulo":                                  # Creamos la condición para verificar si la figura es un rectángulo. 
        base, altura = datos                                    # Creamos las variables base y altura a partir de los datos proporcionados.
        return base * altura                                    # se devuelve el área de un rectángulo, multiplicando la base por la altura.

    elif figura == "circulo":                                   # si la figura es un círculo, se calcula el área utilizando la fórmula que calcula el area del circulo.                           
        (radio,) = datos
        return 3.14159 * (radio ** 2)

    elif figura == "triangulo":                                # si la figura es un triángulo, se calcula el área utilizando la fórmula que calcula el area del triangulo.
        base, altura = datos
        return (base * altura) / 2

    else:                                                      # Si la figura no es reconocida, se devuelve un mensaje indicando que la figura no es válida.
        return "Figura no reconocida"


print(calcular_area("rectángulo", (5, 8)))     # Output: 40
print(calcular_area("circulo", (3,)))          # Output: 28.27431
print(calcular_area("triangulo", (7, 5)))      # Output: 17.5

# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor #a cero). Por ejemplo, descuento de 15€. 
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python


precio = float(input("Introduce el precio original del artículo: "))                   # 1. Solicitamos al usuario que ingrese el precio original de un artículo y lo convertimos a un número flotante para poder realizar cálculos con él.

tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").lower()                # 2. Preguntar si tiene cupón

descuento = 0                                                                          # 3. Si el usuario responde que sí, solicitamos que ingrese el valor del cupón de descuento y lo convertimos a un número float para poder realizar cálculos con él. Si el usuario responde que no, no se aplicará ningún descuento. Si la respuesta no es válida, se mostrará un mensaje indicando que no se aplicará ningún descuento.

if tiene_cupon == "sí" or tiene_cupon == "si":                                         # Se verifica si la respuesta del usuario es "sí" o "si" (en minúsculas para evitar problemas de mayúsculas).
    valor_cupon = float(input("Introduce el valor del cupón: "))                       # Si el usuario tiene un cupón, se solicita que ingrese el valor del cupón y se convierte a un número float.
    
    if valor_cupon > 0:                                                                # Se verifica si el valor del cupón es mayor que cero para determinar si es válido.
        descuento = valor_cupon
    else:                                                                              # Si el valor del cupón no es válido (<=0), se muestra un mensaje indicando que el cupón no es válido y no se aplicará ningún descuento.
        print("Cupón no válido. No se aplicará descuento.")
elif tiene_cupon == "no":                                                              # Si el usuario responde que no tiene un cupón, se muestra un mensaje indicando que no se aplicará ningún descuento.
    print("No se aplicará ningún descuento.")
else:                                                                                  # Si la respuesta del usuario no es ni "sí" ni "no", se muestra un mensaje indicando que la respuesta no es válida y no se aplicará ningún descuento.
    print("Respuesta no válida. No se aplicará descuento.")


precio_final = precio - descuento                                                      # 4. Se calcula el precio final de la compra restando el descuento al precio original del artículo.

if precio_final < 0:                                                                   # Se verifica si el precio final es menor que cero, lo cual no tendría sentido en una compra. Si es así, el precio final se convierte en 0 para no mostrar un importe negativo. 
   precio_final = 0

print("El precio final de la compra es:", precio_final, "€")                           # 5. Se muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él, dependiendo de si el usuario tenía un cupón válido o no. El precio final se muestra en euros (€).


# Ejemplo:
# El precio original del artículo es 100€
# El cupon de descuento es 15€.
# El precio final de la compra es 85€.

# Output:
# Introduce el precio original del artículo: 100
# ¿Tienes un cupón de descuento? (sí/no): sí
# Introduce el valor del cupón: 15
# El precio final de la compra es: 85.0 €