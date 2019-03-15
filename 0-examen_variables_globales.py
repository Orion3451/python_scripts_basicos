'''numero = 15
valor =  [numero if numero > 1 else numero+1]
print (valor)

#VARIABLES GLOBALES
def suma():
    global valor
    valor = 10
    resultado = valor + 5
    return resultado

#valor = 10
resultado = suma()
print (resultado)

def letra(vocal):
    letra_02 = 'b'
    palabra = vocal + letra_02
    return palabra

letra_vocal = 'a'
valor = letra(letra_vocal)
print ('esto es una letra-->{}'.format(valor))
def local():
    #global frase
    global frase
    frase = 'Hola mundo python cambie la frase'
    #print ('aqui entro la variable global-->{}'.format(frase))


frase = 'hola mundo python'
print (frase)
local() # AQUI NO DEBO ASIGNARLE UNA VARIABLE, CASO CONTRARIO NO DEVUELVE
print (frase)'''

def hola():
    global frase
    frase = 'cambie la frase'

frase = 'Hola mundo python '
# NO ASIGNARE UN RETORNO A UNA VARIABLE PARA QUE SOLO SE EJECUTE LA FUNCION
hola()
print (frase)# DEVOLVER SOLO LA PRIMERA VARIABEL ASIGNADA
