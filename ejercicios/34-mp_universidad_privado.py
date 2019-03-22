#CREAR METODOS PRIVADOS PARA UAN CLASE UNIVERSIDAD
#ENCRIPTAR PASSWORD ASUMIMOS EN MAYUSCULAS
#CREAMOS OBJETO MARIO CON NOMBRE PASS CORREO
#HARCODEANDO
#NO SE PUEDE VISUALIZAR PASSWORD NORMALMENTE SI NO ES CON SETTER

# 3. VOLVER PRIVADO PASSWORD Y METODO
class Universidad:
    def __init__(self,nombre,password,correo):
        self.nombre = nombre
        self.__password = self.__encriptar(password)
        self.correo = correo

    def __encriptar(self, password):
        return password.upper()

    def obtener_password(self):
        return self.__password

gary = Universidad('Gary Pommier','secreto','gary@gmail.com')
print(gary.nombre)
print(gary.correo)
print(gary.obtener_password())
