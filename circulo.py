class Circulo:
    pi = 3.1416
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return self.radio*self.radio*Circulo.pi

circulo_uno = Circulo(4)
circulo_dos = Circulo(5)
print circulo_uno.radio
print Circulo.pi
print circulo_uno.area()
