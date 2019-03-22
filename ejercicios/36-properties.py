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
