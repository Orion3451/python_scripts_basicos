def genererador(*args):
    for valor in args:
        yield valor * 10, True, False

for valor in genererador(1,2,3,4,5,6,7,8,9):
    print (valor)
