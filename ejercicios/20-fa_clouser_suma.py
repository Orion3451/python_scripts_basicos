# CLOUSER DE SUMA
def clou_ser():
    def validar():
        return numero_uno > 0 and numero_dos > 0
    return validar

def sumar(mi_clouser):
    if mi_clouser():
        resultado = numero_uno + numero_dos
        print('resultado-->{}'.format(resultado))

#solo se validaran si son mayores a cero
numero_uno = 2
numero_dos = 2
nuevo_clouser = clou_ser()
sumando = sumar(nuevo_clouser)
