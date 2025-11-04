import math

# 1. Imprimir "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Información personal
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

# 4. Cálculo de área y perímetro del círculo
def calcular_area_circulo(radio):
    area_circulo = math.pi * (radio ** 2)
    return f"El área del círculo es de: {area_circulo:.2f}"

def calcular_perimetro_circulo(radio):
    perimetro_circulo = 2 * math.pi * radio
    return f"El perímetro del círculo es de: {perimetro_circulo:.2f}"

# 5. Convertir segundos a horas
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return f"Los segundos ingresados equivalen a {horas:.2f} horas."

# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"\n--- Tabla de multiplicar del {numero} ---")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: división por cero"
    return (suma, resta, multiplicacion, division)

# 8. Cálculo del IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return f"El índice de masa corporal es: {imc:.2f}"

# 9. Conversión de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius}°C equivalen a {fahrenheit:.2f}°F."

# 10. Cálculo de promedio
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return f"El promedio de {a}, {b} y {c} es: {promedio:.2f}"

# -------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------------------------------------------

def main():
    imprimir_hola_mundo()

    # 2. Saludo
    nombre = input("\nIngrese su nombre: ")
    print(saludar_usuario(nombre))

    # 3. Información personal
    print("\nSe imprimirá un mensaje de presentación con su información.")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    residencia = input("Ingrese su lugar de residencia: ")
    print(informacion_personal(nombre, apellido, edad, residencia))

    # 4. Área y perímetro del círculo
    print("\nCalcularemos el área y el perímetro de un círculo.")
    radio = float(input("\nIngrese el radio de un círculo: "))
    print(calcular_area_circulo(radio))
    print(calcular_perimetro_circulo(radio))

    # 5. Segundos a horas
    print("\nConvertiremos segundos a horas.")
    segundos = int(input("\nIngrese una cantidad de segundos: "))
    print(segundos_a_horas(segundos))

    # 6. Tabla de multiplicar
    print("\nRealizaremos una tabla de multiplicar.")
    numero_tabla = int(input("\nIngrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero_tabla)

    # 7. Operaciones básicas
    print("\nRealizaremos las operaciones básicas con 2 números: ")
    a = float(input("\nIngrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    resultados = operaciones_basicas(a, b)
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")

    # 8. Calcular IMC
    print("\nCalculemos un indice de masa corporal.")
    peso = float(input("\nIngrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: (por ejemplo: 1.75) "))
    print(calcular_imc(peso, altura))

    # 9. Conversión de temperatura
    print("\nConvirtamos de grados celsius a fahrenheit.")
    celsius = float(input("\nIngrese una temperatura en °C: "))
    print(celsius_a_fahrenheit(celsius))

    # 10. Promedio de tres números
    print("\nCalculemos un promedio")
    n1 = float(input("\nIngrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    n3 = float(input("Ingrese el tercer número: "))
    print(calcular_promedio(n1, n2, n3))


# -------------------------------------------------------------------
# Ejecución del programa principal
# -------------------------------------------------------------------
if __name__ == "__main__":
    main()
