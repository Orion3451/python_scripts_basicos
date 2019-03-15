def decorador(func):
    def nueva_funcion(*args,**kwargs):
        print ('--------------')
        func()
        print ('--------------')
    return nueva_funcion
@decorador
def saluda():
    print ('Hola Mario te saludo')
    
saluda()
