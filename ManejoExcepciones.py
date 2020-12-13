def divide_elementos_de_lista(lista,divisor):
    return [i/divisor for i in lista]

lista=list(range(10))
divisor=2
print(divide_elementos_de_lista(lista,divisor))