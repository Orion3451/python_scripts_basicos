class Circulo:
    _pi = 3.1416 # el guin bajo es una convencio para desarrolladores para
    #no tocr la variable
    def __init__(self,radio):
        self.radio = radio

    def area(self):
        return self.radio*self.radio*self.pi
        #return self.radio*self.radio*Circulo.pi

circulo_uno = Circulo(4)
circulo_dos = Circulo(3)
Circulo.pi = 30

print(Circulo.pi)
#print(circulo_uno.radio)
#print(circulo_dos.radio)
#print(circulo_uno.pi)
#print(circulo_dos.pi)
print(circulo_uno.__dict__)
print(circulo_uno.area())
