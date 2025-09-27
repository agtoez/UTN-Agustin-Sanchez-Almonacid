#La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las
#copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que
#utilice listas paralelas (una para titulos[] y otra para ejemplares[]). Cada título debe estar
#vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas.
#Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario
#elija salir.
# Requerimientos del Menú
# 1. Ingresar títulos → Para agregar los títulos iniciales de los libros, el usuario indica la
# cantidad inicial.
# 2. Ingresar ejemplares → Para agregar una cantidad de copias para cada título.
# 3. Mostrar catálogo → Muestra todos los libros y su stock actual.
# 4. Consultar disponibilidad → Busca un título específico y muestra cuántos ejemplares
# hay.
# 5. Listar agotados → Muestra los títulos que tienen 0 ejemplares.
# 6. Agregar título → Permite añadir un nuevo libro y sus ejemplares disponibles al
# catálogo, respetando la sincronía de los índices en las listas.
# 7. Actualizar ejemplares (préstamo/devolución) → Permite modificar el stock de un
# libro, elegido por el usuario, para registrar préstamos o devoluciones.
# - Préstamo -> Disminuye en 1 la cantidad de ejemplares del libro seleccionado,
# si hay unidades suficientes.
# - Devolución -> Aumenta en 1 la cantidad de ejemplares del libro seleccionado.
# 8. Salir → Termina la ejecución del programa.

#Introducción al programa:
print("\n" + "-"*50)
print("||| Sistema de gestión de biblioteca escolar |||")
print("-"*50)
#Declaración de variables.
titulos = []
ejemplares = []

while True:
    print("\n" + "-"*50)
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")
    print("-"*50)

    opcion = int(input("Ingrese el número de la opción: "))

    if opcion == 1:
        cantidad = int(input("¿Cuántos títulos desea ingresar?"))
        for i in range(cantidad):
            titulos.append(input("Ingrese el título: "))
            ejemplares.append(0)

    elif opcion == 2:
        for i in range(len(titulos)):
            print("Título: ", titulos[i])
            ejemplares[i] = int(input("Ingrese la cantidad de ejemplares: "))

    elif opcion == 3:
        for i in range(len(titulos)):
            print(f"Título: {titulos[i]}, Cantidad: {ejemplares[i]}")

    elif opcion == 4:
        busqueda = input("Ingrese el nombre del título para consultar disponibilidad: ")
        if busqueda in titulos:
            posicion = titulos.index(busqueda)
            print(f"Hay {ejemplares[posicion]} ejemplares disponibles.")
        else:
            print("El título no existe.")

    elif opcion == 5:
        agotados = False
        for i in range(len(ejemplares)):
            if ejemplares[i] == 0:
                print(f"{titulos[i]} está agotado.")
                agotados = True
        if not agotados:
                print("Todos los títulos están disponibles.")

    elif opcion == 6:
        titulos.append(input("Ingrese el nuevo título: "))
        ejemplares.append(int(input("Ingrese la cantidad de ejemplares: ")))

    elif opcion == 7:
        actualizacion = input("Ingrese el título a actualizar:")
        if actualizacion in titulos:
            posicion = titulos.index(actualizacion)
            print("1. Préstamo")
            print("2. Devolución")
            subopcion = input("Ingrese 1 para préstamos y 2 para devoluciones.")
            if subopcion == "1":
                if ejemplares[posicion] > 0:
                    ejemplares[posicion] -= 1
                    print("Prestamo registrado.")
                else:
                    print("No hay ejemplares disponibles")
            elif subopcion == "2":
                ejemplares[posicion] += 1
                print("Devolución registrada.")
        else:
            print("El título no existe en el catálogo.")

    elif opcion == 8:
        print("Gracias por utilizar el programa.")
        break

    else:
        print("Opción inválida, intente de nuevo.")
