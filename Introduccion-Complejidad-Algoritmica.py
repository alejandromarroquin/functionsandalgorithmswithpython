import time
import sys

def factorial_iterativo(n):
    respuesta=1
    while n>1:
        respuesta *=n
        n -=1
    return respuesta

def factorial_recursivo(n):
    if n==1:
        return 1
    return n*factorial_recursivo(n-1)

if __name__ == "__main__":
    n=int(input('Ingresa un número: '))
    inicio=time.time()
    factorial_iterativo(n)
    final=time.time()
    print(final-inicio)

    sys.setrecursionlimit(50000)
    inicio=time.time()
    factorial_recursivo(n)
    final=time.time()
    print(final-inicio)