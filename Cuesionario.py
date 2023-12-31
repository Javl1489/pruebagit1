variable1 = input("cual es tu nombre")
edad_str = input("Ingrese su edad: ")
variable3 = input("cual es tu cedula:")
edad = int(edad_str)
if edad < 18:
    print("Lo siento, eres menor de 18 años y se te niega el acceso.")
else:
    print("Bienvenido, tienes 18 años o más. Puedes acceder.")
