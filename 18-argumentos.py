'''def suma(*argumento):
    print(argumento)

resultado = suma()
#print (resultado)
#PARA TUPLAS * UN ASTERISCO
def suma(*argumento): # USAR ARGS COMO CONVENCION
    resultado = 0
    for valor in argumento:
        resultado = resultado + valor
    return resultado

resultado = suma(1,2,3,4,5,6,7,8,9)
print (resultado)'''
# PARA DICCIONARIOS ** DOS ATERISCOS
def suma(**kwargs):
    print (kwargs)
    valor = kwargs.get('valor', 'No contiene el valor')
    print (valor)
    return valor
resultado = suma(valor='eduardo',x=2,y=9,z=True)
print ('me retorna el valor-->{}'.format(resultado))
