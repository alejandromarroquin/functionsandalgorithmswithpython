def primera_letra(lista_de_palabras):
    primeras_letras=[]

    for palabra in lista_de_palabras:
        try:
            assert type(palabra)==str,f'{palabra} no es un String'
            assert len(palabra)>0, 'No se permiten Strings vacios'
            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print(e)
        return primeras_letras

lista_de_palabras=[2,'',"Palabra"]
primera_letra(lista_de_palabras)
