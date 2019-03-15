# -*- coding: utf-8 -*-
# !/usr/bin/env python
mi_cadena = "Viendo una cadena demostrativa"
print (mi_cadena)
print ("está es la posicion en ese punto '",mi_cadena[6],"'")
print ("esta es  cadena de posiciones ",mi_cadena[0:10])
print ("E es una cadena negativa", mi_cadena[-1:-5])
print ("Esta una cadena cambiando",mi_cadena[0:4])
print ("aqui estoy modificandoa, es una cadena cambiando",mi_cadena[:15:2])
print ("aqui estoy modificandoa, es una cadena cambiando",mi_cadena[:6])
print ("aqustoy modificandoa, ES UNA CADENA CAMBIANDO",mi_cadena[:6])
print ("Esta es una cadena cambiando",mi_cadena[:8])
print ("Esta es una cadena cambiando",mi_cadena[:7])

cadenita1 = "Hola Pepe!,"
cadenita2 = "que tengas un buen dia."
cadenita3 = "Disculpa... %s %s " % (cadenita1, cadenita2)
print (cadenita3)
print (cadenita1[-6], cadenita2[-8],cadenita2[-19],cadenita2[-15], "...")
print ("Esta es una cadena cambiando",mi_cadena[::-1])

# ESCRIBIR UNA FUNCIÓN QUE TOME UN CARÁCTER Y DEVUELVA TRUE SI ES UNA VOCAL, DE LO CONTRARIO DEVUELVE FALSE.
caracter = 'z'
if caracter == 'a':
    print ('es una vocal-->{}'.format(caracter))
elif caracter == 'e':
    print ('es la vocal-->{}'.format(caracter))
elif caracter == 'i':
    print ('es la vocal-->{}'.format(caracter))
elif caracter == 'o':
    print ('es la vocal-->{}'.format(caracter))
elif caracter == 'u':
    print ('es la vocal-->{}'.format(caracter))
else:
    print ('es una letra-->{}'.format(caracter))
