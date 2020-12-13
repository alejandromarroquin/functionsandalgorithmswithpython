from os import system
system("cls")
print('--------------Primera Práctica-------------')
numero_1=int(input('Ingresa un número: '))
numero_2=int(input('Ingresa otro número: '))
def suma(a,b):
    total=a+b
    return total
print(f'La suma de los dos números es: {suma(numero_1,numero_2)}')
print('-------------Segunda Práctica-------------')
def nombre_completo(nombre,apellido,inverso=False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'
print(nombre_completo('Alejandro','Marroquin'))
print(nombre_completo('Alejandro','Marroquin',inverso=True))
print(nombre_completo(apellido='Marroquin',nombre='Alejandro'))
print('-----------Tercera Práctica--------------')
def raizCuadradaExacta():
    objetivo=int(input('Ingresa un enetero: '))
    respuesta=0
    while respuesta**2<objetivo:
        respuesta+=1
    if respuesta**2==objetivo:
        print(f'La raíz cuadrada de objetivo es {respuesta}')
    else:
        print('El objetivo no tiene una raíz cuadrada exacta')
def raizCuadradaAproximada():
    objetivo=int(input('Ingresa un número: '))
    epsilon=0.01
    paso=epsilon**2
    respuesta=0.0
    num=0
    while abs(respuesta**2-objetivo)>=epsilon and respuesta<=objetivo:
        print(respuesta**2-objetivo, respuesta)
        respuesta+=paso
        num+=1
    if abs(respuesta**2-objetivo)>=epsilon:
        print(f'No se encontro la raíz cuadrada del objetivo')
    else:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')
def raizCuadradaBusquedaBinaria():
    objetivo=int(input('Ingresa un número: '))
    epsilon=0.01
    bajo=0.0
    alto=max(1.0,objetivo)
    respuesta=(alto+bajo)/2
    while abs(respuesta**2-objetivo)>=epsilon:
        print(f'bajo: {bajo}, alto: {alto}, respuesta: {respuesta}')
        if respuesta**2<objetivo:
            bajo=respuesta
        else:
            alto=respuesta
        respuesta=(alto+bajo)/2
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
opc=0
while opc!=4:
    print('1.- Calcular la raíz cuadrada exacta de un número')
    print('2.- Calcular la raíz cuadrada aproximada de un número')
    print('3.- Calcular la raíz cuadrada a través de buqueda binaria')
    print('4.- Salir')
    opc=int(input('Ingresa una opción del menú: '))
    if opc==1:
        raizCuadradaExacta()
    elif opc==2:
        raizCuadradaAproximada()
    elif opc==3:
        raizCuadradaBusquedaBinaria()
    else:
        break