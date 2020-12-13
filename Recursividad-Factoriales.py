from os import system
system("cls")
def factorial(n):
    """Calcula el factorial de n

    n int>o
    return n!    
    """
    if n==1:
        return 1
    return n*factorial(n-1)
print('-------Calcula el factorial de un número----------')
n=int(input('Ingresa un número entero: '))
print(f'El factorial de {n} es {factorial(n)}')