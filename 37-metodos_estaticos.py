class Circulo:
    ''' CUANDO LE PERTENEZCA A ALGO MUY PUNTUAL\n
        POR EJEMPLO PI LE PERTENECE A TODOS LOS CIRCULOS'''
    @staticmethod
    def pi():
        return 3.1416
    def __init__(self,radio):
        self.radio = radio

    def area(self):
        return self.radio*self.radio#*self.pi()
        return self.radio*self.radio*Circulo.pi()
print(Circulo.pi())
circulo_uno = Circulo(7)
print(circulo_uno.area())
# ESTA CON DUDAS EL DE CODIGO FACILITO
