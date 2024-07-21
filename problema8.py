#Crear una función para calcular el factorila de un número (un entero no negativo)
#factorial: multiplicar todos los números enteros positivos que hay entre ese número y el 1

def factorial_n(n):
    
    if n < 0:
        raise ValueError("El numero debe ser entero no negativo")    
        
    multiplicar = 1
        
    for i in range(1, n+1):
      multiplicar *= i
    
    return multiplicar

print(factorial_n(5))
