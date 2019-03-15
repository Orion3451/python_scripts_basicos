class Television:
    tamano= 42
    color='negro'
    marca='sony'
    modelo=2001
    #Metodos
    def prender(self):
        print 'Esta prendiendo'

    def apagar(self):
        if self.condicion_apagar()==2000:
            print 'Se esta apagando por ser un modelo 2000 de bajo rendimiento'
        else:
            print 'No se puede apagar'

    def condicion_apagar(self):
        return self.modelo


tv_obj=Television()
tv_obj.apagar()
