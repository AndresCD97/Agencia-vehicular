# Descripcion de vehiculos
from abc import ABC, abstractmethod


# Clase base o padre
class vehiculos (ABC):
    def __init__(self, marcas, modelos,):   #atributos
        self.marcas = marcas
        self.modelos = modelos
    @abstractmethod
    def descripcion(self):   # metodo que se aplicara poliformismo para dar descripcion
        pass

#clase hija para tipo moto
class moto(vehiculos):

    def descripcion(self):
        return  f"La moto es una: {self.marcas},modelo {self.modelos}"

#clase hija para tipo automovil
class automovil(vehiculos):

    def descripcion(self):
        return f"El vehiculo es un: {self.marcas},modelo {self.modelos}"


#se crea lista de caracteristica a imprimir
lista= [
    automovil(marcas="Mazda", modelos="2 2010"),
    moto(marcas="Suzuki", modelos="basica"),
    automovil(marcas="ford", modelos="Edge 2013"),
    moto(marcas="", modelos=""),
]

#se utiliza la funcion "for" para que recorra la lista e imprima
for v in lista:
    print(v.descripcion())