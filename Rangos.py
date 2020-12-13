from os import system
system("cls")
#range(comienzo,fin,pasos)
my_range=range(1,10)
print(type(my_range))
for i in my_range:
    print(i)
my_range=range(0,7,2)
my_other_range=range(0,8,2)
print(my_other_range==my_other_range)
print('----------Números pares del 0 al 101---------')
for i in range(0,101,2):
    print(i)
print('---------Números Nones del 0 al 101----------')
for i in range(1,101,2):
    print(i)