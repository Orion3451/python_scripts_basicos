def decorador(mi_funcion):
    def nueva_funcion(*args,**kwargs):
        print ('-----------------')
        mi_funcion(*args,**kwargs)
        print ('------------------')

    return nueva_funcion
@decorador
def dividir(num_uno,num_dos):

    print ('resultado-->{0:.4f}'.format(num_uno/num_dos))

dividir(10,3)
