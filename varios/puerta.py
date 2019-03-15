class Puerta:
    color='negro'
    altura= 15
    material='hierro'
    #Metodos
    def abrir(self):
        print 'Abriendo la puerta'

    def cerrar(self):
        if self.condicion_cerrar()==15 and self.condicion_cerrar()=='madera':
            print 'Cerrando la puerta de 15'
            self.altura-=1
            print self.condicion_cerrar()
            if self.condicion_cerrar()==14:
                print 'Se resto la altura y pudo ingresar'

        elif self.condicion_cerrar()==14:
            print 'Cerrando puerta de 14'
        else:
            print 'No es 15 '


    def condicion_cerrar(self):
        return self.altura

puerta_generica=Puerta()
puerta_generica.abrir()
puerta_generica.cerrar()
