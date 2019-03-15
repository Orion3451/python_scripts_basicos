'''def palindromo(frase):
    frase = frase.replace(' ','')
    return frase == frase[::-1]

frase = 'anita lava la tina'
print (frase)
resultado = palindromo(frase)
print (frase)
print (resultado)


def palindromo():
    nuevo_valor = frase.replace(' ','')
    return nuevo_valor == nuevo_valor[::-1]

frase = 'anita lava la tina'
print (frase)
resultado = palindromo()
print (frase)
print (resultado)'''
def valor_comun():
    global variable_comun
    variable_comun = 'Cambiar valor'
def mostrar_comun():
    print (variable_comun)
def crear_comun():
    global nueva_variable
    nueva_variable = 'esta es una variable global'

crear_comun()
print (nueva_variable)

#variable_comun = 'esto es una variable comun'
#mostrar_comun()
#valor_comun()
#print (variable_comun)
