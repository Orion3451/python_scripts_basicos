def suma(valor01,valor02,valor03):
    return valor01 + valor02 + valor03
def division(valor01,valor02):
    return valor01/valor02
def multiples_valores():
    return 'String', 1, True, 25.6

resultado_1 = division(100,1)
resultado_2 = suma(1,2,3)
resultado_3 = multiples_valores()
cadena, num, boolea, floa = multiples_valores()
cadena_1 = resultado_3[0]
print (resultado_1)
print (resultado_2)
print (cadena_1)
print (cadena, num, boolea, floa)
