#!/usr/bin/python3
'''
Aqui colocamos todo lo que hace el modulo a que contexxto corresponde
'''
__author__ = 'Mario Luis Zapata Larico'
__copyright__ = 'Copyright 2019, topazio'
__credits__ = 'topazio'

__licence__ = 'GLP'
__version__ = '1.0.1'
__maintainer__ = 'Mario Luis Zapata Larico'
__email__ = 'marioluis7526@gmail.com'
__status__ = 'Developer'

def suma(num_uno,num_dos):
    return num_uno+num_dos
def resta(num_uno,num_dos):
    return num_uno-num_dos
def division(num_uno,num_dos):
    return num_uno/num_dos
def multiplicasion(num_uno,num_dos):
    return num_uno*num_dos
def saluda():
    print ('hola')
if __name__=='__main__':# Se esta ejecutando del script pricipal?
    saluda()
