#Creamos una función para definir que es un numero primo
# True si es primo

def es_primo(numero):
    if numero <= 1:
        return False  #numeros menores o iguales 1 NO PRIMOS
    if numero <=3:
        return True
    if numero % 2 == 0 or numero % 3 == 0: #Multiplos 2 y 3 NO PRIMOS
        return False

    i = 5

    while i * i <= numero:
        if numero % i == 0 or numero % (i+2) == 0:
            return False
        i += 6
    return True

# Encontrar todos los numeros primos menores que 100

suma_primos = 0

for i in range(2,100):
    if es_primo(i):
        suma_primos +=i

print(f"La suma de todos los numeros primos menores que 100 es: {suma_primos}")

