'''lista = [] # AQUI CREAMOS NUESTRA LISTA EN BLANCO
for valor in range(0,101):
    lista.append(valor)
print (lista)
'''
#FORMA MAS SENCILLA
lista = [valor for valor in range(0,101) if valor % 2 != 0]
print (lista)
tupla = tuple(valor for valor in range(0,101) if valor % 2 != 0)
print (tupla)
diccionario = { indice:valor for indice, valor in enumerate(lista) if indice < 10}
print (diccionario)
