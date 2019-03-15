class Lapiz:
    #por default def __init__(self,color='amarillo',contiene_borrador=True,usa_grafito=False):
    '''Cuenado queremos que los objetos empiezen con valores establecidos'''
    
    def __init__(self,color,contiene_borrador,usa_grafito):
        self.color = color
        self.contiene_borrador = contiene_borrador
        self.usa_grafito = usa_grafito


    def dibujar(self):
        print('El lapiz esta dibujando')

    def borrar(self):
        if self.validar_borrar():
            print('El lapiz esta borrando')
        else:
            print('No es posible borrar')

    def validar_borrar(self):
        return self.contiene_borrador
lapiz_generico = Lapiz('verde',True,False)
lapiz_generico.dibujar()
lapiz_generico.borrar()
