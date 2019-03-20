#CREAR DOS DICCIONARIO AGREGAR NUEVOS VALORES,
#AGREGAR DATOS
#ACTUALIZAR DATOS
#OBTENER VALOR
#BORRAR ELEMENTOS
#UNIR DICCIONARIOS
diccionario = {'toronja':'Es un citrico',
               'mandarina':'Es un citrico deliciosos',
               'pera':'Es una fruta tipo manzana',
               'manzana':'Es una fruta dulce',
               'sandia':'Es una fruta jugosa'}
diccionario['platano'] = 'Fruta con mucho potasio'
diccionario['mandarina'] = 'Fruta dulce injertada(actualizado)'

valor = diccionario.get('mandarina','No existe')

del diccionario['mandarina']
diccionario_dos = {'honda':'marca de auto buena',
                   'mitsubishi':'marca de auto regular',
                   'toyota':'marca de auto normal'}

diccionario.update(diccionario_dos)
print('Valor de mandarina-->{}'.format(valor))
print('Lista de autos-->{}'.format(diccionario_dos))
print('Lista de frutas-->{}'.format(diccionario))
