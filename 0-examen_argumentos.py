def suma(*args):
    resultado = 0
    ultimo = 0
    for valor in args:
        resultado +=valor
    return resultado

def diccionario(**kwargs):
    print (kwargs)

resultado = suma(1,2,3,4,5,6,6)
res_diccionario = diccionario(valor='un dato', x=9, y=10, z=True)
print (resultado)
