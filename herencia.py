#para definir un metodo tiene que usar self
#raise se usa para iniciar una excepcion, que en excepcion es el error
#def es definir un constructor o clase y la funcion
#self es la referencia de la clase, a los objetos de metodos y atributos del clase
# un double guion bajo es un clase privado, sin no tiene ese guion entonces es publica, es un variable global de la clase
#anotacion cuando dar una caracteristica especifico, es estatico no necesista un objeto para definirlo

#metodo abstracto no tiene un codigo definido 
#super().__init__() para llamar el padre del hijo del codigo
#tambien se puede usar super para llamar el codigo de padre

from abc import abstractmethod

class Vehiculo(object):
    precio_base = 0.0
    llantas = 0

    def __init__(self, kilometros, marca, modelo, anio, vendido):
        self.kilometros = kilometros
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.vendido = vendido

    def precio_venta(self):
        if self.vendido is not None:
            return 0.0
        return 5000 * self.llantas

    def precio_compra(self):
        if self.vendido is None:
            return 0.0
        return self.precio_base - (.10 * self.kilometros)

    @abstractmethod
    def tipo_vehiculo(self):
        pass


class Carro(Vehiculo):
    precio_base = 5000
    llantas = 4

    def tipo_vehiculo(self):
        return 'carro'


class Camion(Vehiculo):
    precio_base = 8000
    llantas = 18

    def tipo_vehiculo(self):
        return 'camion'
    
    def xxx(self):
        print(self.precio_venta())
        print(super().precio_venta())

class Busito(Vehiculo):
    precio_base = 6000
    llantas = 4

    def tipo_vehiculo(self):
        return 'busito'


if __name__ == "__main__":
    x = Camion(50000, "Scania", "LBS141", 2000, None)
    print(x.precio_venta())
    x.xxx()
    # x = Carro(50000, "Honda", "Civic", 2016, None)
# print(x.precio_venta())
