class Usuario:
    def __init__(self,usuario,contrasena,correo):
        self.usuario = usuario
        self.__contrasena = self.__encriptar(contrasena)
        self.correo = correo

    def __encriptar(self, contrasena):
        return contrasena.upper()

    # ME RETORNE ATRIBUTOS PRIVADOS
    def get_contrasena(self):
        return self.__contrasena
usuario_empresa = Usuario('mario','secreto','mario@gmail.com')
print('usuario',usuario_empresa.usuario)
#usuario_empresa.__contrasena = 'Aqui cambio contraseña'
#print('contraseña',usuario_empresa.contrasena)
print('correo',usuario_empresa.correo)
print('correo',usuario_empresa.get_contrasena())
