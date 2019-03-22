# CREAR UNA CLASE GATO JAGUAR CON SUS REPSECTIVAS HERENCIAS
# COMO PADRES FELINO Y ANIMAL
class Animal:
    @property
    def terrestre(self):
        print('es terrestre')
        return True

class Felino(Animal):
    @property
    def desgarra(self):
        print('Esta desgarrando')
        return True
    @property
    def cazan(self):
        print('esta cazando')

class Jaguar(Felino):
    pass

class Gato(Felino):
    @property
    def cazador(self):
        self.cazan

leoncito = Gato()
pardo = Jaguar()
print(leoncito.cazador)
print(pardo.desgarra)
print(leoncito.terrestre)
