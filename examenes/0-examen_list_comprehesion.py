#GENERAR UNA LSITA CON FOR
'''lista = []
for valor in range(0,51):
    lista.append(valor)
print (lista)'''
# GENERAR LIST COMPREHENSION

lista_00 = [valor for valor in range(0,101) if valor % 2 == 0]
lista_01 = tuple(valor for valor in range(0,101) if valor % 2 == 0)
lista_02 = {indice:valor for indice, valor in enumerate(lista_00)}
print (lista_00)
print (lista_01)
print (lista_02)
