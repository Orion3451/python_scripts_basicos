#CREAR METODOS PRIVADOS PARA UAN CLASE USUARIO
#ENCRIPTAR PASSWORD ASUMIMOS EN MAYUSCULAS
class Usuario:
    def __init__(self,nombre,password,correo):
        self.nombre = nombre
        self.__password = self.__encriptar(password)
        self.correo = correo

    def __encriptar(self, password):
        return password.upper()

    def get_password(self):
        return self.__password
#CREAMOS OBJETO MARIO CON NOMBRE PASS CORREO
#HARCODEANDO
mario = Usuario('Mario Luis Zapata','Secreto','mario@gmail.com')
print('Nombre: ',mario.nombre)
#mario.__password = 'NUEVO'
#NO SE PUEDE VISUALIZAR PASSWORD NORMALMENTE SI NO ES CON SETTER
# O UN METODO
#print('Password: ',mario.password)
print('Correo: ',mario.correo)
print('Password: ',mario.get_password())
