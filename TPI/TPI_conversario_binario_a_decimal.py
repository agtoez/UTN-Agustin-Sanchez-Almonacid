# Conversor de decimal a binario y de binario a decimal.
print("||||Conversor de decimal a binario y de binario a decimal.||||")

#Abrimos búcle while
while True:

#Mostramos las opciones
    print("\nIngresá 1 para convertir de decimal a binario.")
    print("Ingresá 2 para convertir de binario a decimal.")
    print("Ingresá 0 para salir.")

#Solicitamos al usuario que ingrese una opción válida.
    try:
        opcion = int(input("Por favor, digite una de las siguientes opciones: [ 0 | 1 | 2 ]: "))

#Si el usuario ingresa un número distinto se noticica. 
    except ValueError:
        print("Opción inválida. Debe ingresar 0, 1 o 2.")
        continue

#Si el usuario elige 0, se interrumpe el programa.
    if opcion == 0:
        print("¡Hasta luego!")
        break

#Si el usuario elige 1, se ingresa a la primera opción del programa.
    elif opcion == 1:

#Se solicita un número decimal, de tipo integer.
        try:
            numero = int(input("Ingrese un número decimal: "))

#Si el tipo de dato es distinto, se notifica al usuario y se vuelve al menú.
        except ValueError:
            print("Error: debe ingresar un número entero.")
            continue

#Se empieza a construir el número binario:
#Se declara la variable binario como una string vacía.
        binario = ""

#Corroboramos si es 0, ya que es igual en ambos sistemas.
        if numero == 0:
            binario = "0"

#Si es distinto a 0, se ejecuta un búcle while, que construye el número binario y lo muestra.
        else:
            while numero > 0:
                resto = numero % 2
                binario = str(resto) + binario
                numero = numero // 2

        print(f"El número en binario es: {binario}")
        print("Puede seguir usando el conversor o salir con 0.")

#Se solicita que ingrese un número binario.
    elif opcion == 2:
        numero = input("Ingresá un número binario: ").strip()

        #Comprobamos que solo tenga 0 y 1:
        if set(numero) <= {"0", "1"} and numero != "":
            decimal = 0
            longitud = len(numero)
            #Construimos y mostramos el número decimal:
            for i in range(longitud):
                digito = int(numero[longitud - 1 - i])
                decimal += digito * (2 ** i)
            print(f"El número en decimal es: {decimal}")
            print("Puede seguir usando el conversor o salir con 0.")
        else:
            print("Error: el número binario solo puede contener 0 y 1.")
    else:
        print("Opción incorrecta, intentá de nuevo.")
