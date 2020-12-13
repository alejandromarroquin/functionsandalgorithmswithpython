#Nueva clase
class Hotel:

    #Atributos de la instancia
    def __init__(self,numero_maximo_de_huespedes,lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes=numero_maximo_de_huespedes
        self.lugares_de_estacionamiento=lugares_de_estacionamiento
        self.huespedes=0
    def añadir_huespedes(self,cantidad_huespedes):
        self.huespedes+=cantidad_huespedes

    def checkout(self,cantidad_huespedes):
        self.huespedes-=cantidad_huespedes
    
    def ocupacion_total(self):
        return self.huespedes

#Instancia
hotel=Hotel(numero_maximo_de_huespedes=50,lugares_de_estacionamiento=23)
opc=0
while opc!=4:
    print("-------Bienvenido a nuestra cadena de hoteles--------")
    print("1.- Entrada de huésped")
    print("2.- Salida de huésped")
    print("3.- Mostrar huéspedes")
    print("4.- Salir")
    opc=int(input('Ingrese una opción del menú: '))
    if opc==1 or opc==2:
        num_huespedes=int(input("Ingrese el número de huéspedes: "))
    if opc==1:
        hotel.añadir_huespedes(num_huespedes)
    elif opc==2:
        hotel.checkout(num_huespedes)
    elif opc==3:
        print(f'\nEl hotel tiene una ocupación de {hotel.ocupacion_total()} huéspedes\n')
    else:
        break