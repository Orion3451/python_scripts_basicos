class Lapiz:#Plantilla
    def __init__(self,color,contiene_borrador,usa_grafito):
        self.color = "amarillo"
        self.contiene_borrador = False
        self.usa_grafito = True


    #Metodos
    def dibujar(self):
        print "Estoy dibujando un Lapiz"
    def borrar(self):
        if self.es_valido_para_borrar():
            print " Estoy borrando"
        else:
            print " No se puede borrar"
    def es_valido_para_borrar(self):
        return self.contiene_borrador # self me ayuda a obtener el atributo
#Esto es un objeto
lapiz_generico = Lapiz("verde", True, True)
#print lapiz_generico.color
lapiz_generico.dibujar()
#lapiz_generico.contiene_borrador = True
lapiz_generico.borrar()
