#Título o cabecera del programa:
print("\n" + "-"*50)
print("||| Sistema de gestión de biblioteca escolar |||")
print("-"*50)

#Declaración de listas:
titulos = []
ejemplares = []

#Despliegue de menú:
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

#Solicitud para que el usuario ingrese una opción
    opcionstr = input("Ingrese el número de la opción: ")
    
    #Validación de dato ingresado:
    if not opcionstr.isdigit():
        print(">> Debe ingresar un número entre 1 y 8.")
        continue
    #Conversión a entero.
    opcion = int(opcionstr)

    # 1. Ingresar títulos iniciales.
    if opcion == 1:
        #Solicitud de cantidad de títulos y validación.
        cantidadstr = input("¿Cuántos títulos desea ingresar?: ")
        if not cantidadstr.isdigit():
            print(">> Debe ingresar un número entero válido.")
            continue
        #Conversión de input en string a integer.
        cantidad = int(cantidadstr)
        #Búcle para agregar los títulos a la lista de títulos, según la cantidad ingresada anterior, validación del nombre.
        for i in range(cantidad):
            titulo = input("Ingrese el título: ").strip()
            if titulo == "":
                print(">> El título no puede estar vacío. Se omite.")
                continue
            titulos.append(titulo)
            #Se agrega 0 a ejemplares como valor predeterminado.
            ejemplares.append(0)

    # 2. Ingresar ejemplares para los títulos ya existentes
    elif opcion == 2:
        #Se avisa en caso de que no hayan títulos aún.
        if len(titulos) == 0:
            print(">> No hay títulos cargados aún.")
        #En caso de haber, actúa de manera semejante a la opción uno, actualizando la cantidad de ejemplares para cada uno de los títulos.
        else:
            for i in range(len(titulos)):
                cantstr = input(f"Título: {titulos[i]} → Cantidad de ejemplares: ")
                if not cantstr.isdigit():
                    print(">> Valor inválido. Se asume 0.")
                    ejemplares[i] = 0
                else:
                    ejemplares[i] = int(cantstr)

    # 3. Mostrar catálogo, se despliega una lista ordenada en: Título y cantidad.
    elif opcion == 3:
        if len(titulos) == 0:
            print(">> Catálogo vacío.")
        else:
            for i in range(len(titulos)):
                print(f"Título: {titulos[i]}, Cantidad: {ejemplares[i]}")

    # 4. Consultar disponibilidad, revisa comparando los nombres, revisando que coincida en la lista el nombre ingresado.
    elif opcion == 4:
        if len(titulos) == 0:
            print(">> Catálogo vacío.")
        else:
            busqueda = input("Ingrese el título a buscar: ").strip()
            #Si encuentra, muestra la cantidad de ejemplares disponibles.
            if busqueda in titulos:
                pos = titulos.index(busqueda)
                print(f"Hay {ejemplares[pos]} ejemplares disponibles.")
            else:
                print(">> El título no existe en el catálogo.")

    # 5. Listar agotados o mostrar que están todos disponibles.
    elif opcion == 5:
        #Si está vacío, muestra catálogo vacío.
        if len(titulos) == 0:
            print(">> Catálogo vacío.")
        #Crea la lista de agotados en caso de encontrar títulos con ejemplares = 0, si no hay agotados, muestra que todos los títulos tienen ejemplares disponibles.
        else:
            agotados = False
            for i in range(len(titulos)):
                if ejemplares[i] == 0:
                    print(f"{titulos[i]} está agotado.")
                    agotados = True
            if not agotados:
                print("Todos los títulos tienen ejemplares disponibles.")

    # 6. Agregar título
    elif opcion == 6:
        #Solicita al usuario el nuevo título.
        titulo = input("Ingrese el nuevo título: ").strip()
        #Valida que el título no esté vacío.
        if titulo == "":
            print(">> El título no puede estar vacío.")
        elif titulo in titulos:
            print(">> El título ya se encuentra en el catálogo.")
        else:
            #Solicita la cantidad de ejemplares disponibles del nuevo libro.
            cant_txt = input("Ingrese la cantidad de ejemplares: ")
            if not cant_txt.isdigit():
                print(">> Cantidad inválida. Se asigna 0.")
                cantidad = 0
            else:
                cantidad = int(cant_txt)
            #Actualiza las listas
            titulos.append(titulo)
            ejemplares.append(cantidad)
            print(">> Título agregado correctamente.")

    # 7. Actualizar ejemplares (préstamo o devolución)
    elif opcion == 7:
        #Verifica catálogo.
        if len(titulos) == 0:
            print(">> Catálogo vacío.")
        #Subopciones de entrada y salida de unidades al inventario.    
        else:
            #Solicita el título del catálogo a actualizar.
            actualizacion = input("Ingrese el título a actualizar: ").strip()
            if actualizacion in titulos:
                pos = titulos.index(actualizacion)
                #Disposición de menú.
                print("1. Préstamo")
                print("2. Devolución")
                subop = input("Ingrese 1 o 2: ")
                #Lógica para salida de unidad del inventario.
                if subop == "1":
                    if ejemplares[pos] > 0:
                        ejemplares[pos] -= 1
                        print(">> Préstamo registrado.")
                #Validación de stock.        
                    else:
                        print(">> No hay ejemplares disponibles para préstamo.")
                #Lógica para la entrada de unidad al inventario.
                elif subop == "2":
                    ejemplares[pos] += 1
                    print(">> Devolución registrada.")
                #Si ingresa una opción inválida, se muestra:    
                else:
                    print(">> Opción inválida en el submenú.")
            #En caso de no existir:        
            else:
                print(">> El título no existe en el catálogo.")

    # 8. Salir e interrumpir el programa.
    elif opcion == 8:
        print("Gracias por utilizar el programa.")
        break

    #Si el usuario no ingresa una opción válida:
    else:
        print(">> Opción inválida. Ingrese un número entre 1 y 8.")
