from os import system
system("cls")
objetivo=int(input('Ingresa un enetero: '))
respuesta=0
while respuesta**2<objetivo:
    respuesta+=1
if respuesta**2==objetivo:
    print(f'La raíz cuadrada de objetivo es {respuesta}')
else:
    print('El objetivo no tiene una raíz cuadrada exacta')