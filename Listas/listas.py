# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.
lista = [9, 6, 4, 5, 3, 10, 9, 6, 2, 1]
total = 0
print(lista)
for elemento in lista:
    total += elemento
print(f"El promedio es de: {total/10}")
valorAlto = max(lista)
print(f"El valor más alto es: {valorAlto}")
valorBajo = min(lista)
print(f"El valor más bajo es: {valorBajo}")
# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.
lista2 = []
count = 0
while count < 5:
    lista2.append(input("Ingrese un producto, (hasta 5)"))
    count += 1

lista2 = sorted(lista2)
print(f"La lista ordenada queda de la siguiente forma: {lista2}")

eliminarProducto = input("Ingrese el nombre del producto que deseé elimnar: ")

if eliminarProducto in lista2:
    lista2.remove(eliminarProducto)
    print(f"Lista actualizada: {lista2}")
else:
    print("El producto no está en la lista.")
    
# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.
import random

numeros = [random.randint(1, 100) for _ in range(15)]
print("Lista de números generados:", numeros)

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("Lista de pares:", pares)
print("Cantidad de pares:", len(pares))

print("Lista de impares:", impares)
print("Cantidad de impares:", len(impares))

# 4) Dada una lista con valores repetidos:
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

datosSinRepetir = []

for e in datos:
    if e not in datosSinRepetir:
        datosSinRepetir.append(e)
print(f"La lista sin datos para repetir es: {datosSinRepetir}")

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.
alumnos = ["Agustín", "Tomás", "Ezequiel", "Eliseo", "Simón", "Alina", "Margarita", "Ana"]
while True:
    print("1: Ingrese 1 para agregar un nuevo estudiante.")
    print("2: Ingrese 2 para eliminar un estudiante.")
    print("0: Ingrese 0 para salir.")


# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

lista6 = [1, 2, 3, 4, 5, 6, 7]
print(lista6[::-1])

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.
lista7 = [
    [26,10],
    [28,13],
    [31,17],
    [34,19],
    [34,16],
    [29,14],
    [31,17],
]



# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.
# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.
# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.