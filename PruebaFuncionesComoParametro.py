from os import system
system('cls')
print('------Llamando la función cada que se necesite------')
def suma(a,b):
    muestra_valores(a,b)
    print(unNumero())
    return a+b
def muestra_valores(a,b):
    return print(f'Los valores ingresados son: {a} y {b}')
def unNumero():
    print('Se ejecuto')
    return 3**2
numero1=int(input('Ingresa num1: '))
numero2=int(input('Ingresa num2: '))
print(f'Resultado {suma(numero1,numero2)}')
