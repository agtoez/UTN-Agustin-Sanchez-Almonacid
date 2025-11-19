# manejo_de_archivos.py -- Programa interactivo para práctica de archivos en Python

from pathlib import Path

# --- Ruta al archivo ---
archivo = Path("./Manejo de archivos/products.txt")

# --- Funciones ---
def read_products_file(filepath):
    productos = []
    if not filepath.exists():
        return productos
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split(',')]
            if len(parts) != 3:
                continue
            nombre, precio, cantidad = parts
            try:
                precio = float(precio)
                cantidad = int(cantidad)
            except ValueError:
                continue
            productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
    return productos

def display_products(productos):
    if not productos:
        print("No hay productos para mostrar.")
        return
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

def append_product_to_file(filepath, nombre, precio, cantidad):
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(f"{nombre},{precio},{cantidad}\n")

def save_products_overwrite(filepath, productos):
    with open(filepath, 'w', encoding='utf-8') as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

def find_product(productos, nombre_buscar):
    for p in productos:
        if p['nombre'].lower() == nombre_buscar.lower():
            return p
    return None

# --- Programa principal ---
def main():
    # Crear archivo inicial si no existe
    if not archivo.exists():
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write("lapicera,2000,30\n")
            f.write("cuaderno,10000,20\n")
            f.write("regla,9000,10\n")

    productos = read_products_file(archivo)

    print("\n=== Lista de productos actuales ===")
    display_products(productos)

    # Agregar producto desde teclado
    print("\nIngresar un nuevo producto (dejar vacío para no agregar):")
    nombre = input("Nombre: ").strip()
    if nombre:
        try:
            precio = float(input("Precio: ").strip())
            cantidad = int(input("Cantidad: ").strip())
            append_product_to_file(archivo, nombre, precio, cantidad)
            print("Producto agregado correctamente (append).")
        except ValueError:
            print("Precio o cantidad inválidos. No se agregó el producto.")

    # Recargar lista y mostrar
    productos = read_products_file(archivo)
    print("\n=== Lista actualizada de productos ===")
    display_products(productos)

    # Buscar producto
    buscar = input("\nIngresar nombre de producto para buscar (vacío para salir): ").strip()
    if buscar:
        encontrado = find_product(productos, buscar)
        if encontrado:
            print(f"Producto encontrado: {encontrado}")
        else:
            print("No existe el producto buscado.")

    # Sobrescribir archivo si se desea
    resp = input("\n¿Deseás sobrescribir el archivo con la lista actual en memoria? (s/n): ").strip().lower()
    if resp == 's':
        save_products_overwrite(archivo, productos)
        print("Archivo sobrescrito correctamente.")

if __name__ == "__main__":
    main()

#Tendría que hacer todo en inglés o todo en castellano...