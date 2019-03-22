class Universidad:
    def __init__(self,nombre,password,correo):
        self.nombre = nombre
        self.__password = self.__encriptar(password)
        self.correo = correo

    def __encriptar(self, password):
        return password.upper()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, valor):
        self.__password = self.__encriptar(valor)


gary = Universidad('Gary Pommier','secreto','gary@gmail.com')
# print(gary.nombre)
# print(gary.correo)
print(gary.password)
gary.password = 'mario cambio'
print(gary.password)
