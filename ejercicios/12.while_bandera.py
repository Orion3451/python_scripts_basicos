# VALIDAR UN NUMERO MAYOR A 0 CON WHILE

bandera = True
dato = int(input('digite un numero'))
while bandera:
    if dato > 0:
        print('Correcto es mayor a cero')
        bandera = False
