

# Si x%2 == 0 es par // si es diferente a cero impar

numeros_ingresados = []
n_pares = []
n_impares = []

while True:
    opcion = input("Desea ingresar un número?: ")

    if opcion.upper() == "SI":
        numero = int(input("Ingrese el número: "))
        numeros_ingresados.append(numero)
        if numero % 2 == 0:
            n_pares.append(numero)
        else:
            n_impares.append(numero)
    
    elif opcion.upper() == "NO":
        print(f"Números ingresados: {numeros_ingresados}")
        print(f"Cantidad de números pares: {len(n_pares)}")
        print(f"Cantidad de números inpares: {len(n_impares)}")
        break

    else:
        print("Comando desconocido, vuelve a intentarlo")

