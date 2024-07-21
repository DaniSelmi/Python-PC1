#Serie de Fibonari
#Numero siguiente es la suma de los dos numeros anteriores
# F(N) = F(N-1)+F(N-2), n>1


def fibonacci(n):
    fib_serie = []
    a, b = 0, 1
        
    while a <= n:
        fib_serie.append(a)
        a, b = b, a + b
    return fib_serie


serie = fibonacci(50)
print(f"Serie de Fibonacci hasta 50: {serie}")




