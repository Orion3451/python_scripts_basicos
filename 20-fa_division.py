def division():

    def validar():
        return numero > 0

    if validar():
        resultado = numero/2
        print(resultado)
    else:
        print('No se pudo validar el numero')

numero = 12
dividiendo = division()
