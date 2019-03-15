class Lapiz:

    color = 'Amarillo'# ATRIBUTOS LLAMAREMSO A LAS CARACTERISTICAS
    contiene_borrador = False
    usa_grafito = True
    #METODOS= ACCIONES QUE REALIZA UN OBJETO
    def dibujar(self):
        print('El lapiz esta dibujando')

    def borrar(self):
        if self.validar_borrar():
            print('El lapiz esta borrando')
        else:
            print('No es posible borrar')

    def validar_borrar(self):
        return self.contiene_borrador

lapiz_generico = Lapiz()
lapiz_generico.dibujar()
lapiz_generico.contiene_borrador = True
lapiz_generico.borrar()
