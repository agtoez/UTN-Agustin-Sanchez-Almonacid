from pathlib import Path

archivo = Path("./Manejo de archivos/products.txt")

def leer_productos():
    productos = []
    if archivo.exists():
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append([nombre, float(precio), int(cantidad)])
    return productos

def mostrar(productos):
    if not productos:
        print("No hay productos.")
    for nombre, precio, cantidad in productos:
        print(f"{nombre} - ${precio} - Cant: {cantidad}")

def agregar_producto(nombre, precio, cantidad):
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(f"{nombre},{precio},{cantidad}\n")

def buscar(productos, nombre):
    for p in productos:
        if p[0].lower() == nombre.lower():
            return p
    return None

def main():
    # Crear archivo inicial si no existe
    if not archivo.exists():
        with open(archivo, "w", encoding="utf-8") as f:
            f.write("lapicera,2000,30\ncuaderno,10000,20\nregla,9000,10\n")

    productos = leer_productos()
    print("\n=== Productos ===")
    mostrar(productos)

    # Agregar
    print("\nAgregar producto (vacío para saltar):")
    nombre = input("Nombre: ").strip()
    if nombre:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        agregar_producto(nombre, precio, cantidad)
        print("Producto agregado.")

    productos = leer_productos()
    print("\n=== Lista actualizada ===")
    mostrar(productos)

    # Buscar
    buscar_nombre = input("\nBuscar producto (vacío para salir): ").strip()
    if buscar_nombre:
        p = buscar(productos, buscar_nombre)
        if p:
            print("Encontrado:", p)
        else:
            print("No existe.")

if __name__ == "__main__":
    main()
