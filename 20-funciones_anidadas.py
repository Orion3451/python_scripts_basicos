'''# PASO 1
def validacion(num_01,num_02):
    return num_01 > 0 and num_02 > 0

def division(num_01,num_02):
    if validacion(num_01_num_02):
        return num_01 / num_02

resultado = division(10,1)
print (resultado)
print (resultado)

# PASO 2 ANIDANDO LA FUNCION
def division(num_01,num_02):
    def validacion():
        return num_01 > 0 and num_02 > 0 # TAREAS COMPLEJAS

    if validacion():
        return num_01 / num_02

resultado = division(10,1)
print (resultado)
print (resultado)

#PASO 3 QUITAMOS LOS IF DE VALIDACION
def division(num_01,num_02):
    #SEGUIMOS ANIDADOS
    def validacion():
        print ("cumple anidacion")
        return num_01 > 0 and num_02 > 0 # TAREAS COMPLEJAS
    # NO ES NECESARIO EL IF, YA ESTA HACIENDO LA COMPRARACION COMO UN BOOLEANO
#    if validacion(): LLAMARLOS A VALIDACION O NO LLAMARLOS ES DEPENDE DE CADA UNO
    #    return num_01 / num_02

resultado = division(10,1)
print ("Resultado final-->{}".format(resultado))'''

#PASO 4 LOS CLOSERS , SON LAS QUE CREAN FUNCIONES
'''def crear_funcion(num_01,num_02):
    #SEGUIMOS ANIDADOS
    def validacion():
        print('validacion completa')
        return num_01 > 0 and num_02 > 0 # TAREAS COMPLEJAS

    print ('validacion entrando-->{} y {}'.format(num_01,num_02))
    return validacion

def aplicar_funcion(func):
    print ('aplicando funcion-->{}'.format(func))
    resultado = func()
    print ('aplicando funcion -->{}'.format(resultado))

nueva_funcion = crear_funcion(10,9)
aplicar_funcion(nueva_funcion)'''
# PASO 5 LIMPIANDO CODIGO
def crear_funcion(num_01,num_02):
    #SEGUIMOS ANIDADOS
    def validacion():
        return num_01 > 0 and num_02 > 0 # TAREAS COMPLEJAS
    return validacion

def aplicar_funcion(func):
    resultado = func()
    print ('aplicando funcion -->{}'.format(resultado))

nueva_funcion = crear_funcion(10,9)
aplicar_funcion(nueva_funcion)
