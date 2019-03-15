''' CREAR UNA CLASE GATO QUE LLEGUE A DORMIR COMER
    JUGAR gatito'''
from random import randrange, choice
class Gato():
    conducta = 'bien'
    comida = True
    _raza = 'felino'
    def __init__(self,color='cafe',edad=2,genero='macho'):
        self.color = color
        self.edad = edad
        self.genero = genero

    def comer(self):
        if self.tiene_hambre():
            print('Esta comiendo')
        else:
            print('No tiene hambre')
        if self.jugar() == 'bien':
            print('Se porto {}'.format(self.conducta))
            print('Merece comer mucho...')
        elif self.jugar() == 'regular':
            print('Se porto regular')
        elif self.jugar() == 'malo':
            print('Se porto mal')
    def jugar(self):
        return self.conducta


    def dormir(self):
        print('Esta durmiendo')

    def tiene_hambre(self):
        return self.comida
bandera = True
salir = 0
while bandera:
    gato_defecto = input('Quieres ingresar datos de gato? (S/N)-->')
    gato_defecto = gato_defecto.upper()
    if gato_defecto == 'S':
        color_gato= input('Color del gato-->')
        edad_gato= int(input('Edad del gato-->'))
        genero_gato= input('Genero del gato-->')
        minino = Gato(color_gato,edad_gato,genero_gato)
        comportamiento =choice(['bien', 'regular', 'malo'])
        Gato.conducta = comportamiento
        minino.comer()
        bandera = False
    elif gato_defecto =='N':
        minino = Gato()
        comportamiento =choice(['bien', 'regular', 'malo'])
        bandera = False
    else:
        print('Digite las opciones qu se le dio...')
        salir +=1
        if salir == 3:
            print('Se le dio {} intentos'.format(salir))
            bandera = False

#Gato.comida = False
#Gato.conducta = comportamiento
#minino.dormir()
#minino.jugar()
#minino.comer()
#print(minino.color)
#print(minino._raza)
