from os import system
system("cls")
print('------------------Primera Práctica------------------')
nombre=input('Ingresa tu nombre: ')
print(f'La longitud de tu nombre es de: {len(nombre)} caracteres')
print(f'La primera letra de tu nombre es: {nombre[0]}')
print(f'La última letra de tu nombre es: {nombre[8]}')
print(f'Las tres primeras letras de tu nombre son: {nombre[:3]}')
print(f'Las letras de tu nombre comenzando por el inicio hasta el final con salto de 2: {nombre[::2]}')#nombre[inicio:fin:salto]
print('-----------------Segunda Páctica-------------------')
nombre=input('Ingresa tu nombre: ')
saludo=f'Hola {nombre} bienvenido a la clase de cadenas y entradas'
print(saludo)
print(f'La longitud del saludo es: {len(saludo)}')
