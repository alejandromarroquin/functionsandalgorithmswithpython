from os import system
system("cls")
print('--------------Primera Práctica-------------')
numero_1=int(input('Ingresa un entero: '))
numero_2=int(input('Ingresa un entero de nuevo: '))

if numero_1>numero_2:
    print('El primer número es mayor que el segundo')
elif numero_1<numero_2:
    print('El segundo número es mayor que el primero')
else:
    print('Los dos números son iguales')
print('--------------Segunda Práctica-------------')
nombre_persona_1=input('Ingresa un nombre: ')
edad_persona_1=int(input(f'Ingresa la edad de {nombre_persona_1}: '))
nombre_persona_2=input('Ingresa un nombre: ')
edad_persona_2=int(input(f'Ingresa la edad de {nombre_persona_2}: '))
if edad_persona_1<edad_persona_2:
    print(f'La persona de mayor edad es: {nombre_persona_2}')
elif edad_persona_1>edad_persona_2:
    print(f'La persona de mayor edad es: {nombre_persona_1}')
else:
    print('Ambas personas tienen la misma edad')

