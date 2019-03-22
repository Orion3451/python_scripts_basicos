#CREAR METODOS PRIVADOS PARA UAN CLASE UNIVERSIDAD
#ENCRIPTAR PASSWORD ASUMIMOS EN MAYUSCULAS
#CREAMOS OBJETO MARIO CON NOMBRE PASS CORREO
#HARCODEANDO
#NO SE PUEDE VISUALIZAR PASSWORD NORMALMENTE SI NO ES CON SETTER

# 2. ENCRIPTAR LOS DATOS DEL PASSWORD
class Universidad:
    def __init__(self,nombre,password,correo):
        self.nombre = nombre
        self.password = self.encriptar(password)
        self.correo = correo

    def encriptar(self, password):
        return password.upper()

gary = Universidad('Gary Pommier','secreto','gary@gmail.com')
print(gary.nombre)
# LASTIMOSAMENTE COMO NO ES PRIVADO LO PUEDO
# CAMBIAR EL PASSWORD A GUSTO
gary.password = 'lo cambie el password xD'
print(gary.password)
print(gary.correo)
