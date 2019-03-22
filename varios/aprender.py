# DEL EJERCICIO ANTERIOR CONVERTIR A PROPIEDAD
# LA VISUALIZACION Y EL CAMBIO DE PASSWORD
# ESTO NO ES JAVA ASI QUE CON PROPERTIES
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

    @password.deleter
    def password(self):
        self.__password = None




gary = Universidad('Gary Pommier','secreto','gary@gmail.com')
print(gary.nombre)
print(gary.correo)
print(gary.password) # PROPERTY
gary.password ='nuevo password'
print(gary.password) # SETTER
del gary.password
print(gary.password) # DELETER
