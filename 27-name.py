#print (__name__)
from calculadora import __name__ as __name__calculadora# Nuestro principal script es __name__calculadora
# ejecutar desde ahi porfavor, caso contrario no se ejecutara nada de aca
# cambiamos el name de calculadora, porque seria el mismo que este archivo y de todas maneras
#se ejecutaria sin razon
print(__name__)
print(__name__calculadora)
def saluda():
    print('Primer script')
#AQUI ESTAMOS VIENDO SI NUESTRO SCRIPT PRINCIPAL ES CALCULADORA
# Estas ejecutando __name__calculadora??? osea es igual a nuestro main??
if __name__calculadora == '__main__':# calculadora es el script principal
#no ejecutes desde aqui porfavor, no ejecutare nada.
    print('{}, es el sript principal'.format(__name__calculadora))
    saluda()

else:
    print('Este , {} , no es el script principal'.format(__name__))
    print('no se ejecutara nada...')
