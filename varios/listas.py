# -*-. conding: utf-8 -*-
# !/usr/bin/env python
# EN UNA LISTA PUEDO AGREGAR REMOVER ADICIONAR DATOS
'''def remover(lista):
    for i in lista:
        if i == 4:
            lista.remove(4)
    return lista
'''
a = [4,2,3,5,1,7,9,4]

for i in a:
    if i == 4:
        a.remove(4)
        print a
resultado = a[::-1]
#IMPRESIONES
print resultado
