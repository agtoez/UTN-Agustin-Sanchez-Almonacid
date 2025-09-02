# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input(f'Ingrese su edad:'))
if (edad >= 18):
    print("Es mayor de edad")


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.
nota = int(input(f'Ingrese su nota:'))
if (nota >= 6):
    print("Aprobado")
else:
    print("Desaprobado")


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.
num = int(input(f"Ingrese un número:"))
if num % 2 == 0: print("Ha ingresado un número par")
else: print("Por favor, ingrese un número par")


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
ed = int(input(f'Ingrese su edad:'))
# ● Niño/a: menor de 12 años.
if ed < 12: print("Usted es un niño/a.")
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
elif ed < 12 and ed < 18: print("Usted es un adolescente.")
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
elif ed >= 18 and ed < 30: print("Usted es un adulto/a joven.")
# ● Adulto/a: mayor o igual que 30 años.
elif ed >= 30: print("Usted es un adulto.")


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.
clave = (input("Ingrese una contraseña entre 8 y 14 caracteres."))
if len(clave) <= 14 and len(clave) >= 8: print("Ha ingresado una contraseña correcta.")
else: print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

if mode(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mean(numeros_aleatorios): print("El sesgo es positivo")
if mode(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mean(numeros_aleatorios): print("El sesgo es negativo")
if mode(numeros_aleatorios) == median(numeros_aleatorios) == mean(numeros_aleatorios): print("Sin sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.
palabra = input (print("Ingrese una palabra:"))
if palabra[-1] == "a" or palabra[-1] == "A" or palabra[-1] == "e" or palabra[-1] == "E" or palabra[-1] == "i" or palabra[-1] == "I" or palabra[-1] == "o" or palabra[-1] == "O": print(f"{palabra}!")
else: print(palabra)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas
nombre = input(print("Ingrese su nombre."))
opcion = int(input(print("Ingrese una opción: 1) Para mayúsculas - 2) Para minúsculas - 3) Solo la primera letra mayúscula")))
if opcion == 1: print(nombre.upper())
if opcion == 2: print(nombre.lower())
if opcion == 3: print(nombre.title())

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
magnitud = float(input(print("Ingrese la magnitud del terremoto.")))
# ● Menor que 3: "Muy leve" (imperceptible).
if magnitud < 3: print("Muy leve")
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
if magnitud <= 3 and magnitud < 4: print("Leve")
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
if magnitud <= 4 and magnitud < 5: print("Moderado")
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
if magnitud >= 5 and magnitud < 6: print("Fuerte")
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
if magnitud >= 6 and magnitud < 7: print("Muy fuerte")
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
if magnitud >= 7: print("Extremo")


# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día: "))

if not (1 <= mes <= 12):
    print("Mes inválido.")
    exit()

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20): estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20): estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20): estacion = "Verano"
    else: estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20): estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20): estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20): estacion = "Invierno"
    else: estacion = "Primavera"
else:
    print("Hemisferio inválido.")
    exit()

print(f"En el hemisferio {hemisferio}, el {dia}/{mes}, es {estacion}.")