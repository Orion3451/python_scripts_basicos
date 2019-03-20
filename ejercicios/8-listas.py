# TENGO MI LISTA
'''Crear una lista en el cual se pueda agregar insertar
   ordenar una lista de enteros y extender ambas listas'''

mi_lista = ['hola', 15, 15.6, True]

print('LISTA-->{}'.format(mi_lista))
palabra = 'Mario Luis'
mi_lista.append(palabra)
print('1. Agregando "{}" --> {}'.format(palabra,mi_lista))

palabra = 'Pompom'
posicion = 2
mi_lista.insert(posicion, palabra)
print ('2. Insertando "{}" en posicion "{}"--> {}'.format(palabra,posicion,mi_lista))

mis_enteros = [1,9,8,2,10,0,44,3]
print('LISTA ENTEROS-->{}'.format(mis_enteros))
mis_enteros.sort()
print ('3. Ordenar--> {}'.format(mis_enteros))

print('EXTENDER AMBAS LISTAS')
mi_lista.extend(mis_enteros)
print ('4. Lista Extendida-->{}'.format(mi_lista))
