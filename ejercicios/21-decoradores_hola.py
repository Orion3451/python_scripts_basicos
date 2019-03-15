#DECORADOR DE HOLA MUNDO
def decorador(mi_funcion):
    def nueva_funcion():
        print('-------------')
        mi_funcion()
        print('-------------')
    return nueva_funcion

@decorador
def hola():
    print('Hola mundo python')

hola()
