#CLOUSER PARA RESTA
def clou_ser():
    def validar():
        return x > 0 and y > 0

    return validar

def restar(mi_clouser):
    resultado = mi_clouser()
    if resultado:
        sumar = x + y
        print('Resultado es -->{}'.format(sumar))

x = 13
y = 15
mi_clouser = clou_ser()
restar(mi_clouser)
