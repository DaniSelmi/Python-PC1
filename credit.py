# 1. Vertificar la legitimidad de la tarjeta

def validar_tarjeta(numero):
    suma = 0
    cant_digitos = len(numero)
    lista_1 = []
    lista_2 = []

    # Recorre los digitos de derecha a izquierda
    for i in range(cant_digitos -1, -1, -1):
        digito = int(numero[i])

        # Multiplicar por 2 los numeros

        if (cant_digitos - i) % 2 == 0:
            digito *= 2

            if digito > 9:
                digito -=9

        suma += digito

    #Verficamos si el resultado termina en 0
    return str(suma[-1]) == "0"

# 2. Identificar el tipo de Tarjeta

def tipo_tarjeta(numero):
    if numero[:2] == "34" or numero[:2] == "37":
        return "AMEX"
    elif numero[:2] == "51" or numero[:2] == "52" or numero[:2] == "53" or numero[:2] == "54" or numero[:2] == "55":
        return "MASTERCARD"
    elif numero[0] == "4":
        return "VISA"
    else:
        return "INVALID"

# 3. Pedir la información de tarjeta

numero = input("Estimado usuario ingrese el número de su tarjeta: ")

if validar_tarjeta(numero):
    tipo = tipo_tarjeta
else:
    tipo = "INVALID"

print(numero)
print(tipo)