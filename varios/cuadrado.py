class MiClase:
    def __init__(self,midato):
        self.set_dato(midato)

        def get_dato(self):
            return self.__dato

    def set_dato(self,midato):
        if isinstance(midato,(int,float)):
            if midato < 0:
                print('entro dato')
                self.__dato = 0
            elif midato > 10:
                self.__dato = 10
            else:
                self.__dato = midato
        else:
            raise ValueError('Dato no valido')


    def cuadrado(self):
        return self.__dato**2
a = MiClase(10)
print('el cuadrado es',a.cuadrado())
a.set_dato(7)
print('el cuadrado es',a.cuadrado())
