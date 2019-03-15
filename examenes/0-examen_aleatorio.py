def crear_funcion():
    def validacion():
        return x > 0 and y > 0
    return validacion

def dividir(mi_funcion):
    if mi_funcion():
        resultado = x/y
    return resultado
x=1
y=2
nuevo_funcion = crear_funcion()
respuesta = dividir(nuevo_funcion)
print(respuesta)
