def generador(*args):
    for valor in args:
        yield valor * 10, valor * 20

for x,y in generador(1,2,3,4,5,6,6):
    print('valor x-->{} valor y-->{}'.format(x,y))
