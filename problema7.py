#N° perfecto es numero entero positivos que es igual
# a la suma de sus divisores positivos (excluyeto el propio numero)

def suma_divisores_propios(numero):
    
    suma = 0
    for i in range(1, numero // 2 + 1):
        if numero % i == 0:
            suma += i
    return suma

def n_perfectos(n):
    perfectos = []

    for i in range(2, n):
        if suma_divisores_propios(i) == i:
            perfectos.append(i)
    return perfectos



