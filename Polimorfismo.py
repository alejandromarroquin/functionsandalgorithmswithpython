class Persona:
    def __init__(self,nombre):
        self.nombre=nombre

    def avanza(self):
        print(f'{self.nombre} anda caminando')

class Ciclista(Persona):
    def __init__(self,nombre):
        super().__init__(nombre)

    def avanza(self):
        print(f'{self.nombre} anda moviendose en su bicicleta')

def main():
    persona=Persona('Alejandro')
    persona.avanza()
    ciclista=Ciclista('Daniela')
    ciclista.avanza()

if __name__ == "__main__":
    main()