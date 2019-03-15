#DECORADOR RESTA
def decorador(mi_funcion):
    def nueva_funcion(*args, **kwargs):
        print('-------RESTA------')
        mi_funcion(*args, **kwargs)
        print('-------FINISH-----')

    return nueva_funcion
@decorador
def resta(num_uno, num_dos):
    resultado = num_uno + num_dos
    print(resultado)


resta(12,13)
