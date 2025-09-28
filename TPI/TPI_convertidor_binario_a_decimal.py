# Conversor de decimal <-> binario (sin try/except, validaciones sencillas)
print("|||| Conversor de decimal a binario y de binario a decimal ||||")

while True:
    print("\nIngresá 1 para convertir de decimal a binario.")
    print("Ingresá 2 para convertir de binario a decimal.")
    print("Ingresá 0 para salir.")

    opcion_txt = input("Por favor, digite una de las opciones [0 | 1 | 2]: ").strip()

    if opcion_txt not in ("0", "1", "2"):
        print("Opción inválida. Debe ingresar 0, 1 o 2.")
        continue

    opcion = int(opcion_txt)

    if opcion == 0:
        print("¡Hasta luego!")
        break

    elif opcion == 1:
        # Decimal -> binario
        dec_txt = input("Ingrese un número decimal (entero, puede ser negativo): ").strip()
        if dec_txt == "":
            print("Error: entrada vacía.")
            continue

        # Chequeo de signo y dígitos
        if dec_txt[0] == "-":
            cuerpo = dec_txt[1:]
            signo = -1
        else:
            cuerpo = dec_txt
            signo = 1

        if cuerpo == "" or not cuerpo.isdigit():
            print("Error: debe ingresar un número entero válido (ej. 42 o -5).")
            continue

        numero = int(dec_txt)
        if numero == 0:
            print("El número en binario es: 0")
            continue

        n = abs(numero)
        binario = ""
        while n > 0:
            resto = n % 2
            binario = str(resto) + binario
            n = n // 2

        if numero < 0:
            binario = "-" + binario

        print(f"El número en binario es: {binario}")
        print("Puede seguir usando el conversor o salir con 0.")

    elif opcion == 2:
        # Binario -> decimal
        bin_txt = input("Ingresá un número binario (solo 0 y 1, opcional '-' al inicio): ").strip()
        if bin_txt == "":
            print("Error: entrada vacía.")
            continue

        if bin_txt[0] == "-":
            cuerpo = bin_txt[1:]
            negativo = True
        else:
            cuerpo = bin_txt
            negativo = False

        if cuerpo == "" or any(ch not in ("0", "1") for ch in cuerpo):
            print("Error: el número binario solo puede contener 0 y 1.")
            continue

        decimal = 0
        for ch in cuerpo:
            decimal = decimal * 2 + int(ch)

        if negativo:
            decimal = -decimal

        print(f"El número en decimal es: {decimal}")
        print("Puede seguir usando el conversor o salir con 0.")
