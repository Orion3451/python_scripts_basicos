diccionario = { 'a' : 55,
                'c' : 'esto es un string'}
diccionario['d'] = 'NUEVO STRING'
diccionario['x'] = 'Agregando mas datos al diccionario'
diccionario['a'] = False #ACTUALIZANDO VALORES
diccionario['x'] = 'Actualziando x'
#valor = diccionario['a']
# METODO DE DICCIONARIO
valor = diccionario.get('z', 'no hay z ') # SI ES QUE NO HAY Z
#ELIMINANDO VALORES
del diccionario['a']
#OBJETOS ITERABLES
llaves = diccionario.keys()
#AGREGANDO MAS DICCIONARIOS
diccionario_02 = {'f':'dato nuevo'}
diccionario.update(diccionario_02)
print (diccionario)
print (valor)
print (llaves)
