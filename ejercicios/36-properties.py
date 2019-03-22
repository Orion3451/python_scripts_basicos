'''class M():

    def __init__(self):
        self._m = None

    @property
    def mmm(self):
        return self._m

    @mmm.setter
    def mmm(self, val):
        self._m = val

    @mmm.deleter
    def mmm(self):
        print('deleting') # Not printing
        del(self._m)


if __name__ == '__main__':

    i = M()
    i.mmm = 150
    print(i.mmm)
    del(i.mmm)
    print(i.mmm)'''
class Usuario:
    def __init__(self,usuario,contrasena,correo):
        self.usuario = usuario
        self.__contrasena = self.__encriptar(contrasena)
        self.correo = correo

    def __encriptar(self, contrasena):
        return contrasena.upper()

    @property
    def contrasena(self):
        return self.__contrasena

    @contrasena.setter
    def contrasena(self, valor):
        self.__contrasena = self.__encriptar(valor)

mario = Usuario('mario','secreto','mario@gmail.com')
print(mario.contrasena)
mario.contrasena = 'nuevo password'
print(mario.contrasena)
