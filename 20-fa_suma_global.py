# CON VARIABLES GLOBALES
def suma():
    global resultado
    def validar():
        return numero_dos > 0 and numero_uno > 0
    if validar():
        resultado = numero_uno + numero_dos

#solo se validaran si son mayores a cero
numero_uno = 2
numero_dos = 2
sumando = suma()
print('resultado-->{}'.format(resultado))
