#RECORRER UNA LISTA NUMERICA CON FOR
# Y UNA CADENA
lista_numero = [1,2,3,4,5,6,7]
cadena = 'Hola Mario'
for valor in lista_numero:
    print (valor)

for indice, valor in enumerate(lista_numero):
    print(indice,valor)

print (len(lista_numero))
