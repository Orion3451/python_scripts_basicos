'''
try:
    print (2/0)
except ZeroDivisionError as ex:
    print(ex)
    print('No es posible dividir entre cero')

print('Se termino el script')'''

try:
    lista = [1,2]
    print(lista[1])
except IndexError as ex:
    print('Error de indexado')
except ZeroDivisionError as ex:
    print(ex)
    print('No es posible dividir entre cero')
finally:
    
    print('Se termino el script')
