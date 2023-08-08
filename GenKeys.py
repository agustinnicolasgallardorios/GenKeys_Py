print ("bienvenidos al generador de contraseñas")
ing_password_1 = (input("Ingrese una contraseña: "))

class password():

    def __init__ (self, password_ing, password_1):

        self.password_ing = password_ing
        self.password_1 = password_1

    def generador_keys(self):
        print(" las opciones posibles son: ")
        print("opcion_a: ",self.password_ing, self.password_1)

    def generador_keys_2(self):
        print("opcion_b: ",self.password_ing, self.password_1)

    def generador_keys_3(self):
        print("opcion_c: ",self.password_ing, self.password_1)

contra_ing = password (ing_password_1, "123")
contra_ing.generador_keys()

contra_ing2 = password (ing_password_1, "abcif")
contra_ing2.generador_keys_2()

contra_ing3 = password (ing_password_1, "trukini_23")
contra_ing3.generador_keys_3()



ing_password = (input("¿cual desea selecionar? "))

opciona = "opcion_a"
opcionb = "opcion_b"
opcionc = "opcion_c"
cuenta = 0

while cuenta < 2:

    if ing_password == opciona:
     print("la contraseña final sera: ", ing_password_1, "123")
     print("que tenga un buen dia!")
     break

    elif ing_password == opcionb:
     print("la contraseña final sera: ", ing_password_1, "abcif")
     print("que tenga un buen dia!")
     break

    elif ing_password == opcionc:
     print("la contraseña final sera: ", ing_password_1, "trukini23")
     print("que tenga un buen dia!")
     break

    else:
     print("por favor ingrese un valor correcto, a los dos intentos, la cuenta sera bloqueada")
     print("que tenga un buen dia!")
     ing_password = (input("ingrese nuevamente, un valor: "))
    cuenta += 1

    if cuenta == 2:
       print("su cuenta fue bloqueada, contactase con soporte")
       
mensaje = float(input(" "))
    



