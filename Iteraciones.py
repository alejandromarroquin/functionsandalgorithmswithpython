from os import system
system("cls")
print('----------------Primera Práctica (while)-----------------')
contador_externo=0
contador_interno=5
while contador_externo<5:
    while contador_interno>0:
        print(f'{contador_externo}: {contador_interno}')
        contador_interno-=1
    contador_externo+=1
    contador_interno=5
print('---------------Segunda Práctica (for)---------')
frutas = ['manzana', 'pera', 'mango']
for fruta in frutas:
    print(fruta)
print('--------------Tercera Práctica (for)----------')
iter('cadena') # cadena
iter(['a', 'b', 'c']) # lista
iter(('a', 'b', 'c')) # tupla
iter({'a', 'b', 'c'}) # conjunto
iter({'a': 1, 'b': 2, 'c': 3}) # diccionario
iterator=iter(frutas)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print('-------------Cuarta Práctica (for con diccionarios)------------')
estudiantes={
    'México':10,
    'Colombia':17,
    'Puerto Rico':20,
}
print(f'Paises de los estudiantes: ')
for pais in estudiantes:
    print(pais)
print(f'Paises de los estudiantes: ')
for pais in estudiantes.keys():
    print(pais)
print(f'Número de estudiantes: ')
for num_estudiantes in estudiantes.values():
    print(num_estudiantes)
print('Número de estudiantes por país: ')
for pais, num_estudiantes in estudiantes.items():
    print(f'En {pais} hay {num_estudiantes} alumnos')