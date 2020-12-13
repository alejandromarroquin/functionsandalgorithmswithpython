from os import system
system("cls")
my_dic={
    'David':35,
    'Fanny':22,
    'Valeria':21,
    'Iridian':23
}
print(my_dic)
print(my_dic['David'])
print('-----Acceder a un elemento si no sabemos si existe en el diccionario----')
print('El elemento no se encuentra en el diccionario')
print(my_dic.get('Juan',30))
print('El elemento si se encuentra en el diccionario')
print(my_dic.get('David',30))
print('--------Borrar un elemento del diccionario-----')
del my_dic['Iridian']
print(my_dic)
print('------Iterar sobre las llaves del diccionario--------')
for llave in my_dic.keys():
    print(llave)
print('------Iterar sobre los valores del diccionario--------')
for valor in my_dic.values():
    print(valor)
print('------Iterar sobre las llaves y valores del diccionario--------')
for item in my_dic.items():
    print(item)
print('------Consultar si una llave se encuentr en el diccionario--------')
print('Fernanda' in my_dic)
print('Valeria' in my_dic)
print('*************Diccionarios Comprehension****************')
tiendita={
    'Jitomate':20,
    'Cebolla':12,
    'Aguacate':40,
    'Lechuga':8
}
double_prices=[price*2 for price in tiendita.values()]
print(double_prices)
print([price*2 for price in tiendita.values() if price*2<=50])