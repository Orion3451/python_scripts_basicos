def generador(*args):
    '''recibe n cantidad de numeros
    y las devuelve si es mayor
    '''
    for valor in args:
        yield valor, True if valor > 5 else False
nombre = generador.__name__
documentacion = generador.__doc__
print (nombre,':')
print (documentacion)
# INTERPRETE from import 23-docstrings
