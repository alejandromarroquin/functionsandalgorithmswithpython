print('---------Declarar lista-------')
my_list=[1,2,3]
print('------Mostrar el valor de un indice de la lista------')
print(my_list[0])
print('------Obtener un fragmento de la lista-------')
print(my_list[1:])
print('------Agregar un elemento a una lista-------')
my_list.append(4)
print('--------Imprimir lista-----------')
print(my_list)
print('------Reasignar el valor de un indice de la lista-----')
my_list[0]='a'
print('------Imprimir la nueva lista------------')
print(my_list)
print('-----------Sacar el último elemento de la lista-----')
my_list.pop()
print('-----Imprimir la nueva lista-----')
print(my_list)
print('------Iterar sobre los elementos de una lista-----')
for element in my_list:
    print(element)
print('******Ejemplo de Efectos Secuendarios al mutar listas********')
a=[1,2,3]
b=a
c=[a,b]
print(a)
print(b)
print(c)
a.append(4)
print(a)
print(b)
print(c)
print('************Clonación***********')
a=[1,2,3]
c=list(a)
print(id(a))
print(id(c))
print('**********List comprehension********')
my_list=list(range(100))
print(my_list)
double=[i*2 for i in my_list]
print(double)
pares=[i for i in my_list if i%2==0]
print(pares)