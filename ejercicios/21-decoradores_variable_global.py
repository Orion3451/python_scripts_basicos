#DECORADOR VARIABLE GLOBAL
# SOLO DEBO UAR VARIABLES GLOBALES
# CUANDO SE DECLARE UNA CONSTANTE O ALGO SENCILLO
def decorador(mi_funcion):
    def nueva_funcion(*args, **kwargs):
        resultado = mi_funcion(*args, **kwargs)
    return nueva_funcion

@decorador
def sumar(n_uno, n_dos):
    resultado = n_uno + n_dos
    print('Resultado-->{}'.format(resultado))

num_uno = 15
num_dos = 20
sumar(num_uno, num_dos)
