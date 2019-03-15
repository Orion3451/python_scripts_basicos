# CON VARIABLES
# ES MAS REBUNDANTE EL CODIGO CON SOLO VDARIABLES
def suma(x,y):
    def validar(x,y):
        return x > 0 and y > 0
    if validar(x,y):
        resultado = x + y
    return resultado

#solo se validaran si son mayores a cero
numero_uno = 2
numero_dos = 2
sumando = suma(numero_uno,numero_dos)
print('resultado-->{}'.format(sumando))
