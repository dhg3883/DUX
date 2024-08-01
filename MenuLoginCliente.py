from Cliente import *

def generamenulogin():
    correolectronicofe = input("Escriba el correo electronico para el ingreso")
    clavefe   = input("Escriba la clave para el ingreso")
    nuevocliente = Cliente()
    nuevocliente.correolectronico = correolectronicofe
    nuevocliente.clave = clavefe
    if nuevocliente.login().cedula != "-1":
        print("Bienvenido " + nuevocliente.nombre)
    else:
        print("Eres hacker?...")

           