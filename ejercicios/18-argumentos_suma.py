#REALIZAR UNA SUMA CON DICCIONARIOS
def suma(**kwargs):
    suma = 0
    for indice, valor in kwargs.items():
        suma = valor + suma
    return suma

#HARDCODEANDO
resultado = suma(valor=2,x=2,z=2)
print(resultado)
