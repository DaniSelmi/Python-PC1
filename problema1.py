
inicio = 1500
fin = 2700

numeros_validos = []

for num in range(inicio,fin + 1):
    if num % 7 == 0 and num % 5 == 0:
        numeros_validos.append(num)

print("Números divisible por 7 y múltiplos de 5 en el rango de 1500 a 2700")

for numero in numeros_validos:
    print(numero)