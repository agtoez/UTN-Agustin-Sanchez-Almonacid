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
    print("\nLista actual de alumnos:")
    print(alumnos)
    
    print("\n1: Agregar un nuevo estudiante")
    print("2: Eliminar un estudiante existente")
    print("0: Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nuevo = input("Ingrese el nombre del nuevo estudiante: ").strip()
        if nuevo:  # verifica que no esté vacío
            alumnos.append(nuevo)
            print(f"✅ {nuevo} fue agregado correctamente.")
        else:
            print("⚠️ No se ingresó ningún nombre.")

    elif opcion == "2":
        eliminar = input("Ingrese el nombre del estudiante a eliminar: ").strip()
        if eliminar in alumnos:
            alumnos.remove(eliminar)
            print(f"🗑️ {eliminar} fue eliminado correctamente.")
        else:
            print("⚠️ Ese nombre no está en la lista.")

    elif opcion == "0":
        print("\nSaliendo del programa...")
        break

    else: print("⚠️ Opción no válida. Intente nuevamente.")

print("\nLista final actualizada:")
print(alumnos)


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

promMin = sum(t[0] for t in lista7) / len(lista7)
promMax = sum(t[1] for t in lista7) / len(lista7)

amplitudes = [t[1] - t[0] for t in lista7]
diaMayorAmplitud = amplitudes.index(max(amplitudes)) + 1

print(f"Promedio mínimas: {promMin}")
print(f"Promedio máximas: {promMax}")
print(f"Mayor amplitud térmica: Día {diaMayorAmplitud}")


# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

# Matriz de notas: filas = estudiantes, columnas = materias
notas = [
    [7, 8, 6],
    [5, 9, 8],
    [6, 7, 7],
    [8, 6, 9],
    [9, 8, 10]
]

# Promedio de cada estudiante
print("Promedio de cada estudiante:")
for i, estudiante in enumerate(notas):
    promedio = sum(estudiante) / len(estudiante)
    print(f"Estudiante {i+1}: {promedio:.2f}")

# Promedio de cada materia
print("\nPromedio de cada materia:")
num_materias = len(notas[0])
for j in range(num_materias):
    suma = sum(notas[i][j] for i in range(len(notas)))
    promedio = suma / len(notas)
    print(f"Materia {j+1}: {promedio:.2f}")
    
# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
    print()

def ta_te_ti():
    tablero = [["-" for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    turno = 0
    movimientos = 0
    print("Tablero inicial:")
    mostrar_tablero(tablero)
    while movimientos < 9:
        jugador = jugadores[turno % 2]
        print(f"Turno del jugador {jugador}")
        try:
            fila = int(input("Ingrese la fila (0, 1, 2): "))
            columna = int(input("Ingrese la columna (0, 1, 2): "))
            if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == "-":
                tablero[fila][columna] = jugador
                mostrar_tablero(tablero)
                turno += 1
                movimientos += 1
            else:
                print("Movimiento inválido. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
    print("Fin del juego (sin verificación de ganador).")

ta_te_ti()

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.
def tateti():
    tablero = [["-" for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    turno = 0

    for _ in range(9):
        mostrar_tablero(tablero)
        jugador = jugadores[turno % 2]
        print(f"Turno de {jugador}")
        try:
            fila = int(input("Ingrese la fila (0, 1, 2): "))
            col = int(input("Ingrese la columna (0, 1, 2): "))
            if 0 <= fila < 3 and 0 <= col < 3 and tablero[fila][col] == "-":
                tablero[fila][col] = jugador
                turno += 1
            else:
                print("Posición inválida, intente de nuevo.")
                continue
        except ValueError:
            print("Entrada inválida, intente de nuevo.")
            continue
    mostrar_tablero(tablero)

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.