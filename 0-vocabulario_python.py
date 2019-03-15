diccionario = {'instancia':'', 'peudocodigo':''}
bandera = 1
while bandera:
    contador = int(input('Cuantas palabras desea agregar?'))
    print ('Ok, se agregaran {} palabras.'.format(contador))
    for valor in range(contador):
        registrar = input('Agrege palabra-->')
        definicion = input('Definicion-->')
        diccionario[registrar] = definicion
    bandera = False


print (list(diccionario.keys()))
