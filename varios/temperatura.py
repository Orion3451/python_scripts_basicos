class Celsius:
    def __init__(self, temperature):
        self.__temperature = self.__to_fahrenheit(temperature)

    def __to_fahrenheit(self, valor):
        return (valor* 1.8) + 32

    @property
    def temperature(self):
        print("Obteniendo valor")
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            print("Temperature below -273 is not possible")
        print("Colocando valor")
        self.__temperature = value

temp_obj = Celsius(-275)
print(temp_obj.temperature)
temp_obj.temperature = -274
print(temp_obj.temperature)
