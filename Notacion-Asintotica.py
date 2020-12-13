# Ley de la suma

def f1(n):
    for i in range(n):
        print(i)
    
    for i in range(n):
        print(i)

# o(n)+o(n)=o(n+n)=o(2n)=o(n) -> La función crece en o(n)

def f2(n):
    for i in range(n):
        print(i)
    
    for i in range(n*n):
        print(i)
#o(n)+o(n*n)=o(n+n**2)=o(n**2) -> La función crece en o(n**2), es decir, está función es cuadratica

# Recursividad múltiple
def fibonacci(n):
    if n==0 or n==1:
        return 1;
    return fibonacci(n-1)+fibonacci(n-1)

# o(2**n) -> El crecimiento es exponencial