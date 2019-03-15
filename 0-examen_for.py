#https://www.facebook.com/bisonimbus.gro.9?__tn__=%2CdCH-R-R&eid=ARAXkrzMEkRHYvwzA5MAO2blKqPoS-oUXL8__WDYUWOdkB3RByRk96twvGFtmaUoIkjHrSgMZ67vNXTb&hc_ref=ARQL1ZufWKVpgN3p1xrznGWU4ybUrBqy2S372e0lEEk_g8T6y-Fy2_QzCXJPjm1Hak8&fref=nf
#Escriba un programa que pida dos números enteros y escriba qué números son pares
#y cuáles impares desde el primero hasta el segundo.
bandera = True
num_uno = int(input('Digite un numero-->'))
while bandera:
    num_dos = int(input('Digite un numero mayor a {}--> '.format(num_uno)))
    if num_dos > num_uno:
        bandera = False
for valor in range(num_uno,num_dos+1):
    if valor % 2 == 0:
        print ('{} es un numero par'.format(valor))
    else:
        print ('{} es un numero impar'.format(valor))
