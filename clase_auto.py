#HACER UNA CLASE DE AUTO QUE ACELERE Y FRENE
#Y UNA CONDICION PARA ACELERAR
class Auto:
    #atributos
    color = 'blanco'
    marca = 'toyota'
    año = '1998'
    registrado = True
    gasolina = False
    #METODOS
    def acelerar(self):
        print('estamos acelerando')

    def frenar(self):
        if self.validar_frenar():
            print('Hay gasolina, no frene')
        else:
            print('No hay gasolina frene')

    def validar_frenar(self):
        return self.gasolina

corriendo = Auto()
corriendo.marca
corriendo.acelerar()
corriendo.gasolina = True
corriendo.frenar()
