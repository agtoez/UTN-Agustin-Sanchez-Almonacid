# 1) Agregar frutas al diccionario.

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# precios_frutas['Naranja'] = 1200
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300

# print(precios_frutas)

# # 2) Actualizar precios

# precios_frutas['Banana'] = 1330
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melon'] = 2800

# print(precios_frutas)

# # 3) Listar frutas

# frutas = list(precios_frutas.keys())

# print(frutas)

# # 4) Programa números telefónicos:

# telefonos = {}

# for i in range(5):
#     nombre = input("Nombre del contacto: ")
#     numero = input("Número telefónico: ")
#     telefonos[nombre] = numero

# buscar = input("Ingresá el nombre a buscar: ")

# if buscar in telefonos:
#     print("El número es:", telefonos[buscar])
# else:
#     print("No se encontró ese contacto.")

# # 5) Palabras únicas + conteo de palabras

# frase = input("Ingresá una frase: ").lower()

# palabras = frase.split()

# #Palabras únicas
# unicas = set(palabras)
# print("Palabras únicas:", unicas)

# # Diccionario con cantidad de veces que aparece cada palabra.

# frecuencias = {}

# for palabra in palabras:
#     if palabra in frecuencias:
#         frecuencias[palabra] += 1
#     else:
#         frecuencias[palabra] = 1

# print("Frecuencia de palabras: ", frecuencias)

# # 6) Alumnos con tupla de notas + promedio

# alumnos = {}

# for i in range(3):
#     nombre = input("Nombre del alumno: ")
#     nota1 = float(input("Nota 1: "))
#     nota2 = float(input("Nota 2: "))
#     nota3 = float(input("Nota 3: "))
#     alumnos[nombre] = (nota1, nota2, nota3)

# for nombre, notas in alumnos.items():
#     promedio = sum(notas) / 3
#     print(f"{nombre} tiene un promedio de {promedio:.2f}")

# # 7) Mostrar los que aprobaron ambos parciales, (operaciones con sets):

# parcial1 = {1, 2, 3, 5, 6, 7}
# parcial2 = {2, 3, 4, 6, 7}

# ambos = parcial1 & parcial2
# print("Aprobaron ambos: ", ambos)

# solo_uno = parcial1 ^ parcial2
# print("Aprobaron solo uno:", solo_uno)

# al_menos_uno = parcial1 | parcial2
# print("Aprobraron al menos uno: ", al_menos_uno)

# # 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.

# stock = {
#     "café": 10,
#     "pan": 20,
#     "yerba": 15
# }

# #Consultar stock
# producto = input("Ingresar producto a consultar: ")

# if producto in stock:
#     print(f"Stock disponible: {stock[producto]}")
# #Agregar unidades al stock si el producto existe
#     agregar = int(input("¿Cuántas unidades agregar?: "))
#     stock[producto] += agregar
# #Agregar un nuevo producto si no existe.
# else:
#     print("Producto no existente. Se agregará al sistema.")
#     cantidad = int(input("Ingresar cantidad inicial: "))
#     stock[producto] = cantidad
# print("Stock actualizado:", stock)