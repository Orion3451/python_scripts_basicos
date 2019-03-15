# los datos seran modificados por la clase y no por la instancia.
class Usuario:
    def __init__(self,username,password,email):
        self.username = username
        self.__password = self.__generar_password(password)# metodo privado
        self.email = email
    def __generar_password(self,password):
        return password.upper()

    @property
    def password(self):
        return self.__password

mario = Usuario('mario','mario123','mario@gmail.com')
print mario.username
print mario.email
print mario.password
mario.__password='aqui cambio'

print mario.password
