'''import random
valor_cero = random.randint(0,10)
print(valor_cero)
lista = [True, 'String', 23, False]
for x in range(0,10):
    valor = random.choice(lista)
    print ('Aleatorio-->{}'.format(valor))
random.shuffle(lista)
print(lista)
'''
#import datetime BUSCAR EN CODIGO FACILITO EL VIDEO
import sys
import time

for i in range(100):
    time.sleep(0.5)
    sys.stdout.write('\r%d %%' % i) # el signo porcentaje es doble para imprimir
    sys.stdout.flush()
