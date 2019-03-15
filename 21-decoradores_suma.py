#DECORADOR DE HOLA MUNDO
def decorador(mi_funcion):
    def nueva_funcion(*args, **kwargs):
        print('-------------')
        solucion = mi_funcion(*args, **kwargs)
        print('-------------')

        return solucion

        print('-------------')
    return nueva_funcion

@decorador
def sumar(num_uno,num_dos):
    resultado = num_uno + num_dos
    return resultado

x = 12
y = 12
respuesta = sumar(x,y)
print('respuesta-->{}'.format(respuesta))
