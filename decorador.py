
def decorador(func):# A, B
    def nueva_funcion():
        print "vamos a ejecutar funcion"
        func()
        print "se ejecuto la funcion"
    return nueva_funcion #C

@decorador
def saluda():
    print 'hola mundo'
@decorador
def suma():
    print 10+10
suma()
saluda()
