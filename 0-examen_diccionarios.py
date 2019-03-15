#ASIGANRLE VALORES A UN DICCIONARIO
diccionario = { 'a': 'Esto es una cadena ', 'b':'Esto es otra cadena', 5:'esto es un entero', (1,2):'Esto es una tupla'}
#DICCIONARIO CRECER Y DECRECER
diccionario['x'] = 'nuevo valor'
#MODIFICAR VALOR ACTUALIZAR DATOS
diccionario['a'] = 'Actualizando datos de a'
#OBTENER VALORES DEL DICCIOANRIO
valor = diccionario['a']

# EN CASO DE ERROR MOSTRAR OTRO VALOR RECOMENDADO GET
valor01 = diccionario.get('z','boosting')
valor02 = diccionario.get('a',(1,2))
# BORRAR UN VALOR DE DICCIONARIO
del diccionario['a']
del diccionario['b']
#OBJETO ITERABLE
#RETORNAR, VALORES LISTAS TUPLAS , PURAS
llaves00 = diccionario.keys()
llaves01 = list(diccionario.keys())
llaves02 = tuple(diccionario.keys())
#CRECER DICCIONARIO AGREGAR OTRO DICCIONARIO
diccionario_01 = {'f':'nuevos valores', 6:'entero nuevo', (3,2):'tupla nueva'}
diccionario.update(diccionario_01)

#IMPRESIONES
print (diccionario)
print ('obteniendo valor--->',valor)
print ('obteniendo con get ---> ',valor01)
print ('obteniendo valor nuevo---.>{}'.format(valor02))
print ('obteniendo llaves--->{}'.format(llaves00))
print ('obteniendo llaves lista--->{}'.format(llaves01))
print ('obteniendo llaves tupla--->{}'.format(llaves02))
print ('Este es el nuevo diccionario--->{}'.format(diccionario_01))
print (' este es el diccionario original actualizado--->{}'.format(diccionario))
