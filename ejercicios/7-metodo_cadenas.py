#!/usr/bin/env python
# -*- coding: utf-8 -*-
#UNIR DOS CADENAS HACER BUSQUEDA Y CONVERTIR AH MAYUSCULAS
#In python2:

#raw_input(): It takes exactly what user type and passes it back as string object.

#input(): It takes exactly what used typed and then convert the type of entered object. Example. used entered [10,20,30], then it will return as List object type.

#In Python3:

#input(): It is exactly same as raw_input() in Python2.

#eval(input()): It is exactly same as input() in Python2.
curso = "El curso"
mi_string = "Aplicando el curso de codigo facilito"
result = "{} de {}".format(mi_string,curso)
#CONVERTIR A MAYUSCULA
#result = result.upper()
print (result)
res_curso = curso.find('curso')
print ('palabra encontrada CF --.>{}'.format(res_curso))
'''
#BUSQUEDA
result = result.find('curso')
print (result)'''

#CONVERTIR A MINUSCULA
resultado = result.lower()
print (resultado)

oracion_00 = 'esta es una oracion y se buscara una palabra especifica dentro el codigo'
oracion_01 = 'esta es otra oracion para la busqueda de palabras y letras'
oracion_unir = '{},{}'.format(oracion_00,oracion_01)
print ('oracion unida-->{}'.format(oracion_unir))
busqueda = oracion_00.find('y')
print ('Palabra encontrada--> {}'.format(busqueda))
mayusculas = oracion_unir.upper()
print ('Convertido a mayusculas-->{}'.format(mayusculas))
