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
# 4) Dada una lista con valores repetidos:
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.
# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.
# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).
# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.
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