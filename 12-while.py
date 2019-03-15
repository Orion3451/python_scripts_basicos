contador = 0
while contador < 10:
    print (contador)
    contador += 1
    if contador == 5:
        print  ('estamos en-->{}'.format(contador))
    if contador == 6:
        break
else:
    print ('El while ah terminado')

contador_01 = 0
bandera_01 = True
while bandera_01:
    print (contador_01)
    contador_01 += 1
    if contador_01 == 5:
        print  ('estamos en-->{}'.format(contador_01))
    if contador_01 == 6:
        bandera_01 = False
else:
    print ('El while ah terminado')
