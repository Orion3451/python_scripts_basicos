#CREAR METODOS PRIVADOS PARA UAN CLASE UNIVERSIDAD
#ENCRIPTAR PASSWORD ASUMIMOS EN MAYUSCULAS
#CREAMOS OBJETO MARIO CON NOMBRE PASS CORREO
#HARCODEANDO
#NO SE PUEDE VISUALIZAR PASSWORD NORMALMENTE SI NO ES CON SETTER

# 1. CREAR OBJETO UNIVERSIDAD Y MOSTRAR SUS DATOS
class Universidad:
    def __init__(self,nombre,password,correo):
        self.nombre = nombre
        self.password = password
        self.correo = correo

gary = Universidad('Gary Pommier','secreto','gary@gmail.com')
print(gary.nombre)
print(gary.password)
print(gary.correo)
