# -*- coding: utf-8 -*-
#!/usr/bin/env python
#EXAMEN DE METODO DE CADENAS.
#unir cadenas con format y volverlas mayusculas y minusculas, buscar
#palabras dentro la cadena concatenada
mi_palabra = 'La union es la fuerza'
mi_palabra_2 = 'Soló se que nada se'
uniendo = 'Estoy uniendo dos palabras {} y {}'.format(mi_palabra,mi_palabra_2)
# ASIGNANDO VARIABLE A UNIENDO
imp_uniendo = uniendo
# CONVIERTO A MAYUSCULA
may_uniendo = uniendo.upper()
# BUSCANDO
bus_uniendo = uniendo.find('ES')
print 'encontrando valor bus_uniendo {}'.format(bus_uniendo)
if bus_uniendo == -1:
    print 'no se encontro ES'
# REEMPLAZAR
reem_uniendo = uniendo.replace('ó','XXXX')
#IMPRESIONES
print imp_uniendo
print may_uniendo
print bus_uniendo
print reem_uniendo
