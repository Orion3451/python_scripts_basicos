#Escriba un programa que pida dos números enteros.
#El programa pedirá de nuevo el segundo número mientras no sea mayor que el primero.
#El programa terminará escribiendo los dos números.
bandera = True
while bandera:
    numero_alto = int(input('Digite un numero-->'))
    if numero_alto == '':
        numero_alto = 1
        bandera = False
    else:
        bandera = False
bandera = True
while bandera:
    # COLOCAR INT PORQUE SINO PYTHON LO CONSIDERA UNA CADENA EN EL IF
    numero_bajo = int(input ('Digite numero menor a {}-->'.format(numero_alto)))
    if numero_bajo == '':
        numero_bajo = 0
        bandera = False
    elif numero_bajo <= numero_alto:
        bandera = False
    else:
        print ('el numero {} es mayor a {}, intente denuevo...'.format(numero_bajo,numero_alto))

print ('Los numeros son {} y {}'.format(numero_alto, numero_bajo))
