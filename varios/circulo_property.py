class Circulo_uno:

    def __init__(self, radio):
        self.radio = radio

    @property
    def dame_area(self):
        return 3.14159 * (self.radio ** 2)

c1= Circulo_uno(20)
print(c1.dame_area)
