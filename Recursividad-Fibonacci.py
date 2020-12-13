from os import system
system("cls")
def fibonacci(n):
    '''
    Devuelve la serie de fibonacci desde 1,1,2, hasta un número n de términos

    :param n: int > 3 terminos de la serie
    :return:  serie de fibonnaci
    '''
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

opcion = int(input("Términos de la serie: "))
for i in range(opcion):
    print(fibonacci(i))