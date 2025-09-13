# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(1, 101):
    print(i)
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
num = int(input("Ingrese un número para calcular la cantidad de dígitos."))
cantDigitos = len(str(num))
print(f"El número: {num}, tiene: {cantDigitos} dígitos.")
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
entre = int(input("Ingrese el número desde el que quiere sumar(Este no se sumará):"))
hasta = int(input("Ingrese el número hasta el que quiere sumar(Este tampoco se sumará):"))
total = 0
for i in range(entre, hasta):
    i+1
    total += i
print(f"El total de la suma de los enteros entre: {entre}; hasta: {hasta}; es: {total}")
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
tot = 0
n = int(input("Ingrese un número distinto a 0 para inicializar la suma, (este no se sumará): "))
if (n > 0):
    while(n != 0):
        n = int(input("Ingrese un número distinto a 0, ingrese 0 para finalizar."))
        tot = tot + n
    print(f"El total es: {tot}")
else:
    print("El número debe ser distinto a 0.")
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
nAl = random.randint(0, 9)
nU = 10
acum = 0
while(nU != nAl):
    nU = int(input(print("Intente adivinar el número ingresando enteros entre 0 y 9: ")))
    acum += 1
print(f"Has acertado, el número es: {nAl} y ha tomado: {acum} intentos")
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
for i in range(1, 102):
    print(i - 1)
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
hta = int(input("Ingrese el número hasta el que quiere sumar:"))
totalHta = 0
for i in range(0, hta):
    i + 1
    totalHta += i
print(f"El total de la suma de los enteros entre: 0; hasta: {hta}; es: {totalHta}")
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
numero = 0
cantNumero = 0
numPar = 0
numImpar = 0
numNeg = 0
numPos = 0

while(cantNumero <= 9):
    numero = int(input("Ingrese un número entero: "))
    if (numero > 0): numPos += 1
    elif (numero < 0): numNeg += 1

    if (numero % 2 == 0): numPar += 1
    elif (numero % 2 != 0): numImpar += 1
    cantNumero += 1
print(f"Resultados: n\ Cantidad de números positivos: {numPos} n\ Cantidad de números negativos: {numNeg} n\ Cantidad de números pares: {numPar} n\ Cantidad de números impares: {numImpar}" )

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
tot9 = 0 
cantidad = 10

for i in range(cantidad):
    n9 = int(input(f"Ingrese el número {i+1} de {cantidad}: "))
    tot9 += n9

media = tot9 / cantidad
print(f"La media de los {cantidad} números ingresados es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.