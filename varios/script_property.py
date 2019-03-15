'''class Celsius:
    def __init__(self, temperatura = 0):
        self.temperatura = temperatura

    def a_farenheit(self):
        return (self.temperatura * 1.8) + 32

#Creando nuevo objeto
termometro = Celsius()
#colocando temperatura
termometro.temperatura = 37
#obtener temperatura
print(termometro.temperatura)
# obtener conversion a a_farenheit
print('{0:.2f}'.format(termometro.a_farenheit()))
print(termometro.__dict__)'''
class Celsius:
    def __init__(self, temperatura = 0):
        self.colocar_temperatura(temperatura)

    def a_farenheit(self):
        return (self.obtener_temperatura() * 1.8) + 32
    #actualizando
    def obtener_temperatura(self):
        return self._temperatura

    def colocar_temperatura(self, valor):
        if valor < -273:
            raise ValueError('Temperatura inexistente por dbajo de -273')
        self._temperatura = valor

#Creando nuevo objeto
termometro = Celsius(-272)
#termometro.colocar_temperatura(10) tambien podemos enviar a la variablede clase
#nuestra temperatura que estamos enviando es de 272
print(termometro.obtener_temperatura())
#termometro.colocar_temperatura(10)
#print(termometro._temperatura)
#termometro._temperatura= -300
#termometro.get_temperatura()
