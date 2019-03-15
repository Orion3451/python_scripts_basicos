from modulos_calculadora import resta,multiplicasion, division
'''from modulos_calculadora import (suma,
                                 resta,
                                 multiplicasion,
                                 division)
#from modulos_calculadora import * = import modulos_calculadora no es convencional hacer esto
'''
from modulos_calculadora import suma as sum
resultado_cero = sum(10,4)
resultado_uno = resta(10,4)
resultado_dos = multiplicasion(10,4)
resultado_tres = division(10,4)
print ('suma-->{}'.format(resultado_cero))
print ('resta-->{}'.format(resultado_uno))
print ('multiplicasion-->{}'.format(resultado_dos))
print ('division-->{0:.2f}'.format(resultado_tres))
