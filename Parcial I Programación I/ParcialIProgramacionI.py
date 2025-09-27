print("\n" + "-"*50)
print("||| Sistema de gestión de biblioteca escolar |||")
print("-"*50)

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

    opcionstr = input("Ingrese el número de la opción: ")
    if not opcionstr.isdigit():
        print(">> Debe ingresar un número entre 1 y 8.")
        continue
    opcion = int(opcionstr)

    # 1. Ingresar títulos iniciales
    if opcion == 1:
        cantidadstr = input("¿Cuántos títulos desea ingresar?: ")
        if not cantidadstr.isdigit():
            print(">> Debe ingresar un número entero válido.")
            continue
        cantidad = int(cantidadstr)
        for i in range(cantidad):
            titulo = input("Ingrese el título: ").strip()
            if titulo == "":
                print(">> El título no puede estar vacío. Se omite.")
                continue
            titulos.append(titulo)
            ejemplares.append(0)

    # 2. Ingresar ejemplares para los títulos ya existentes
    elif opcion == 2:
        if len(titulos) == 0:
            print(">> No hay títulos cargados aún.")
        else:
            for i in range(len(titulos)):
                cantstr = input(f"Título: {titulos[i]} → Cantidad de ejemplares: ")
                if not cantstr.isdigit():
                    print(">> Valor inválido. Se asume 0.")
                    ejemplares[i] = 0
                else:
                    ejemplares[i] = int(cantstr)

    # 3. Mostrar catálogo
    elif opcion == 3:
        if len(titulos) == 0:
            print(">> Catálogo vacío.")
        else:
            for i in range(len(titulos)):
                print(f"Título: {titulos[i]}, Cantidad: {ejemplares[i]}")

    # 4. Consultar disponibilidad
    elif opcion == 4:
        if len(titulos) == 0:
            print(">> Catálogo vacío.")
        else:
            busqueda = input("Ingrese el título a buscar: ").strip()
            if busqueda in titulos:
                pos = titulos.index(busqueda)
                print(f"Hay {ejemplares[pos]} ejemplares disponibles.")
            else:
                print(">> El título no existe en el catálogo.")

    # 5. Listar agotados o mostrar que están todos disponibles.
    elif opcion == 5:
        if len(titulos) == 0:
            print(">> Catálogo vacío.")
        else:
            agotados = False
            for i in range(len(titulos)):
                if ejemplares[i] == 0:
                    print(f"{titulos[i]} está agotado.")
                    agotados = True
            if not agotados:
                print("Todos los títulos tienen ejemplares.")

    # 6. Agregar título
    elif opcion == 6:
        titulo = input("Ingrese el nuevo título: ").strip()
        if titulo == "":
            print(">> El título no puede estar vacío.")
        else:
            cant_txt = input("Ingrese la cantidad de ejemplares: ")
            if not cant_txt.isdigit():
                print(">> Cantidad inválida. Se asigna 0.")
                cantidad = 0
            else:
                cantidad = int(cant_txt)
            titulos.append(titulo)
            ejemplares.append(cantidad)
            print(">> Título agregado correctamente.")

    # 7. Actualizar ejemplares (préstamo o devolución)
    elif opcion == 7:
        if len(titulos) == 0:
            print(">> Catálogo vacío.")
        else:
            actualizacion = input("Ingrese el título a actualizar: ").strip()
            if actualizacion in titulos:
                pos = titulos.index(actualizacion)
                print("1. Préstamo")
                print("2. Devolución")
                subop = input("Ingrese 1 o 2: ")
                if subop == "1":
                    if ejemplares[pos] > 0:
                        ejemplares[pos] -= 1
                        print(">> Préstamo registrado.")
                    else:
                        print(">> No hay ejemplares disponibles para préstamo.")
                elif subop == "2":
                    ejemplares[pos] += 1
                    print(">> Devolución registrada.")
                else:
                    print(">> Opción inválida en el submenú.")
            else:
                print(">> El título no existe en el catálogo.")

    # 8. Salir
    elif opcion == 8:
        print("Gracias por utilizar el programa.")
        break

    else:
        print(">> Opción inválida. Ingrese un número entre 1 y 8.")
