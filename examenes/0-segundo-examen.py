#ASIGANRLE VALORES A UN DICCIONARIO
diccionario_frutas = {'manzana':'esta es rica de color rojo',
    'mandarina':'esta es un citrico delicioso',
    'uva':'de sabor espectacular',
    10:'cantidad de frutas actuales',
    (1,2):'hay 1 de cada dos'}
#DICCIONARIO CRECER Y DECRECER AUMENTANDO MAS FRUTAS UNO A UNO
diccionario_frutas['toronja'] = 'es una fruta muy acida pero rica'
#MODIFICAR UN VALOR SIGNIFICA ACTUALIZAR DATOS
diccionario_frutas['uva'] = 'Actualizando la uva, es muy rica'
#OBTENER VALORES DEL DICCIONARIO
# EN CASO DE ERROR MOSTRAR OTRO VALOR RECOMENDADO GET
#valor = diccionario_frutas['mandarina'] no es la forma correcta pero igual funciona
valor = diccionario_frutas.get('mandarina','no se encontro la fruta')


# BORRAR UN VALOR DE DICCIONARIO
del diccionario_frutas['manzana']
#CRECER DICCIONARIO AGREGAR OTRO DICCIONARIO
diccionario_verduras = {'huacataya':'es una verdura saborisante',
                        'perejil':'para la sopa',
                        'morron':'para la sopa saborisar',
                        'tomate':'indispensable'}
diccionario_frutas.update(diccionario_verduras)
#IMPRESIONES
print ('mi diccionario frutas--->{}'.format(diccionario_frutas))
print ('datos de mandarina--->{}'.format(valor))
print ('este es diccionario verduras--->{}'.format(diccionario_verduras))
