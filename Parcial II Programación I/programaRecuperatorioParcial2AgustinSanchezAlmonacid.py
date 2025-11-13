#Importamos dependencias
import csv
import os

ARCHIVO_CSV = "catalogo.csv"

# Funciones útiles.---

def normalizarTitulo(titulo):
    # Normaliza el título para comparar sin mayúsculas ni espacios redundantes
    return " ".join(titulo.strip().lower().split())

def buscarLibro(catalogo, titulo):
    # Busca un libro por título normalizado. Devuelve el diccionario o None
    tituloNormal = normalizarTitulo(titulo)
    for libro in catalogo:
        if normalizarTitulo(libro["TITULO"]) == tituloNormal:
            return libro
    return None

def validarEnteroPositivo(valor):
    # Devuelve True si el valor de un número entero >= 0.
    return valor.isdigit() and int(valor) >= 0

# Persistencia---

def cargarCatalogo():
    # Si existe, se carga el catálogo desde un archivo CSV SIN try/except
    catalogo = []
    if os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, newline='', encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                cantidad_txt = fila.get("CANTIDAD", "").strip()

                # Validación SIN try/except
                if cantidad_txt.isdigit():
                    cantidad = int(cantidad_txt)
                else:
                    cantidad = 0   # Si no es válido, se normaliza a 0

                titulo = fila.get("TITULO", "").strip()
                if titulo:  # solo se agregan títulos válidos
                    catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
    return catalogo

def guardarCatalogo(catalogo):
    # Guarda el catálogo actual en el archivo CSV    
    with open(ARCHIVO_CSV, "w", newline='', encoding="utf-8") as f:
        campos = ["TITULO", "CANTIDAD"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for libro in catalogo:
            escritor.writerow(libro)

#Funcionalidades---

def ingresarTitulos(catalogo):
    n = input("¿Cuántos libros desea ingresar? ")
    if not n.isdigit() or int(n) <= 0:
        print("Cantidad inválida.\n")
        return
    n = int(n)

    for _ in range(n):
        while True:
            titulo = input("Título: ").strip()
            if not titulo:
                print("El título no puede estar vacío.")
                continue
            if buscarLibro(catalogo, titulo):
                print("El título ya existe en el catálogo.")
                continue

            cantidad = input("Cantidad de ejemplares: ")
            if not validarEnteroPositivo(cantidad):
                print("Debe ingresar un número entero mayor o igual a 0.")
                continue

            catalogo.append({"TITULO": titulo, "CANTIDAD": int(cantidad)})
            print(f"Libro '{titulo}' agregado correctamente.\n")
            break

    guardarCatalogo(catalogo)
    print("Catálogo actualizado y guardado.\n")

def ingresarEjemplares(catalogo):
    titulo = input("Título del libro: ")
    libro = buscarLibro(catalogo, titulo)

    if not libro:
        print("Título no encontrado.\n")
        return

    cant = input("Cantidad de ejemplares a agregar: ")
    if not cant.isdigit() or int(cant) <= 0:
        print("Debe ingresar un número entero mayor que 0.\n")
        return

    libro["CANTIDAD"] += int(cant)
    guardarCatalogo(catalogo)
    print(f"Se agregaron {cant} ejemplares a '{libro['TITULO']}'.\n")

def mostrarCatalogo(catalogo):
    print("\n|--- Catálogo actual ---|")
    if not catalogo:
        print("No hay libros cargados.")
    else:
        for libro in catalogo:
            print(f"- {libro['TITULO']} → {libro['CANTIDAD']} ejemplares")
    print()

def consultarDisponibilidad(catalogo):
    titulo = input("Título a consultar: ")
    libro = buscarLibro(catalogo, titulo)
    if libro:
        print(f"Disponibles de '{libro['TITULO']}': {libro['CANTIDAD']} ejemplares.\n")
    else:
        print("Título no encontrado.\n")

def listarAgotados(catalogo):
    print("\n--- Libros agotados ---")
    agotados = [l for l in catalogo if l["CANTIDAD"] == 0]

    if agotados:
        for l in agotados:
            print(f"- {l['TITULO']}")
    else:
        print("No hay libros agotados.")
    print()

def agregarTitulo(catalogo):
    titulo = input("Nuevo título: ").strip()
    if not titulo:
        print("El título no puede estar vacío.\n")
        return
    if buscarLibro(catalogo, titulo):
        print("El título ya existe en el catálogo.\n")
        return

    cantidad = input("Cantidad de ejemplares: ")
    if not validarEnteroPositivo(cantidad):
        print("Debe ingresar un número entero mayor o igual a 0.\n")
        return

    catalogo.append({"TITULO": titulo, "CANTIDAD": int(cantidad)})
    guardarCatalogo(catalogo)
    print(f"Libro '{titulo}' agregado correctamente.\n")

def actualizarEjemplares(catalogo):
    titulo = input("Título: ")
    libro = buscarLibro(catalogo, titulo)
    if not libro:
        print("Título no encontrado.\n")
        return

    accion = input("¿Préstamo (P) o Devolución (D)? ").strip().upper()

    if accion == "P":
        if libro["CANTIDAD"] > 0:
            libro["CANTIDAD"] -= 1
            print(f"Préstamo registrado. Restan {libro['CANTIDAD']}.")
        else:
            print("No hay ejemplares disponibles para préstamo.")
    elif accion == "D":
        libro["CANTIDAD"] += 1
        print(f"Devolución registrada. Ahora hay {libro['CANTIDAD']}.")
    else:
        print("Opción inválida. Debe ingresar P o D.")
        return

    guardarCatalogo(catalogo)
    print()

# Menú principal---

def menu():
    catalogo = cargarCatalogo()
    print("=== SISTEMA DE BIBLIOTECA ESCOLAR ===\n")

    while True:
        print("Menú de opciones:")
        print("1. Ingresar títulos (múltiples)")
        print("2. Ingresar ejemplares")
        print("3. Mostrar catálogo")
        print("4. Consultar disponibilidad")
        print("5. Listar agotados")
        print("6. Agregar título individual")
        print("7. Actualizar ejemplares (préstamo/devolución)")
        print("8. Salir")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1": ingresarTitulos(catalogo)
            case "2": ingresarEjemplares(catalogo)
            case "3": mostrarCatalogo(catalogo)
            case "4": consultarDisponibilidad(catalogo)
            case "5": listarAgotados(catalogo)
            case "6": agregarTitulo(catalogo)
            case "7": actualizarEjemplares(catalogo)
            case "8":
                print("Gracias por usar el sistema.")
                break
            case _:
                print("Opción inválida. Intente nuevamente.\n")

# ---------------- EJECUCIÓN ----------------

if __name__ == "__main__":
    menu()
