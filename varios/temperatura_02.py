class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        print('Obteniendo temperatura')
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print('Colocando temperatura ')
        self._temperature = value

#c = Celsius(-277)
c = Celsius(37)
print(c.get_temperature())
#print(c.set_temperature(-300))
print(c.set_temperature(10))
c._temperature = -300
print(c.get_temperature())
