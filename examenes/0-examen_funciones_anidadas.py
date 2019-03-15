'''def division(num_uno, num_dos):
    def validacion():
        return num_uno > 0 and num_dos > 0
    if validacion():
        return num_uno / num_dos
    else:
        print ('No se puede dividir')
resultado = division(10,2)
print (resultado)'''
# APLICANDO CLOUSTER

def creando_funcion(num_uno, num_dos):
    def validacion():
        if num_uno > 0 and num_dos > 0:
            return num_uno / num_dos
    return validacion

def aplicando_funcion(funcion_enviada):
    resultado = funcion_enviada()
    print ('funcion exito-->{}'.format(resultado))

nueva_funcion = creando_funcion(10,2)
aplicando_funcion(nueva_funcion)
