class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

#create new object
man = Celsius()
# set temperature
man.temperature = 37
print(man.temperature)
# get degress Fahrenheit
print(man.to_fahrenheit())
print(man.__dict__)
