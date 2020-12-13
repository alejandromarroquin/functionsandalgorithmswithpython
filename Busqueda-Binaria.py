import random

def busqueda_binaria(lista,inicio,final,objetivo):
    print(f'Buscando {objetivo} entre {lista[inicio]} y {lista[final-1]}')
    if inicio>final:
        return False
    mitad=(inicio+final)//2
    if lista[mitad]==objetivo:
        return True
    elif lista[mitad]<objetivo:
        return busqueda_binaria(lista,mitad+1,final,objetivo)
    elif lista[mitad]>objetivo:
        return busqueda_binaria(lista,inicio,mitad-1,objetivo)

if __name__ == "__main__":
    tamaño_de_lista=int(input('Ingresa el tamaño de la lista: '))
    objetivo=int(input('Ingrese el número objetivo: '))
    lista=sorted([random.randint(0,100) for i in range(tamaño_de_lista)])
    print(lista)
    encontrado=busqueda_binaria(lista,0,len(lista),objetivo)
    print(f'El elemento {objetivo} {"Si esta" if encontrado else "No esta"}')