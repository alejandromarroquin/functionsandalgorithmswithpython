import random
def busqueda_lineal(lista,objetivo):
    match=False
    for elemento in lista:
        if elemento==objetivo:
            match=True
            break
    return match

if __name__ == "__main__":
    tamaño_de_la_lista=int(input('Ingrese el tamaño de la lista: '))
    objetivo=int(input('Ingresa el número que deseas encontrar: '))
    lista=[random.randint(0,100) for i in range(tamaño_de_la_lista)]
    print(lista)
    encontrado=busqueda_lineal(lista,objetivo)
    print(f'El elemento {objetivo} {"Si esta" if encontrado else "No esta"}')