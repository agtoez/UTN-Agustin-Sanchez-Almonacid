#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:      # Caso base
        return 1
    return n * factorial(n - 1)   # Recursión

num = int(input("Ingrese un número: "))

for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Ingrese posición límite de la serie del número fibonacci: "))

for i in range(num + 1):
    print(fibonacci(i), end=" ")

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
#algoritmo general.

def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

b = int(input("Base: "))
e = int(input("Exponente: "))
print(f"{b}^{e} =", potencia(b, e))

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Número decimal: "))
binario = decimal_a_binario(num)
print("Binario:", binario if binario != "" else "0")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Palabra: ").lower()
print(es_palindromo(texto))

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    if n < 10:             # Caso base
        return n
    return (n % 10) + suma_digitos(n // 10)

num = int(input("Número: "))
print("Suma de dígitos:", suma_digitos(num))

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

num = int(input("Bloques del nivel inferior: "))
print("Total de bloques:", contar_bloques(num))

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)


num = int(input("Número: "))
d = int(input("Dígito a buscar: "))
print("Aparece:", contar_digito(num, d), "veces")

