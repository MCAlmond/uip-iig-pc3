

class Figuras(object):
    lado = 0
    radio = 0

    def area(self):
        if self.lado > 0:
            return(self.lado**2)
        
        if self.radio > 0:
            return(3.1416*self.radio**2)
        

class Circulo(Figuras):
    def __init__ (self,radio):
         self.radio = radio
         self.lado = 0

    def circunferencia(self):
        circ = 2*3.1416*self.radio
        return circ


class Cuadrado(Figuras):
    def __init__ (self, lado):
         self.radio = 0
         self.lado = lado

    def perimetro(self):
        per = self.lado*4
        return per


if __name__ == '__main__':
    circulo = Circulo(22)
    cuadrado = Cuadrado(34)

    print(circulo.circunferencia())
    print(circulo.area())

    print(cuadrado.perimetro())