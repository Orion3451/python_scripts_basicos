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

class Mascota:
    nombre = '' # Todas las mascotas tienen un nombre
    @property
    def mostrar_nombre(self):
        print(self.nombre)
class Gato(Felino, Mascota):
    @property
    def cazador(self):
        self.cazan

leoncito = Gato()
leoncito.nombre = 'Pishico'
leoncito.mostrar_nombre
