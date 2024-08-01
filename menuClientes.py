from Cliente import *

def generamenu():
    while True: 
        print("Presiona 1 para guardar un nuevo cliente")
        print("Presiona 2 para listar los clientes guardados")
        print("Presiona 4 para eliminar")
        print("Presiona 5 para modificar")
        print("Presiona 3 Salir")
        opcion = input()
        if opcion == "1":
            cedulafe = input("Escriba la cedula del nuevo cliente")
            nombrefe = input("Escriba el nombre del nuevo cliente")
            pafe = input("Escriba el primer apellido del nuevo cliente")
            safe = input("Escriba el segundo apellido del nuevo cliente")
            direccionfe = input("Escriba la direccion del nuevo cliente")
            correolectronicofe = input("Escriba el correo electronico del nuevo cliente")
            tipofe = input("Escriba el tipo del nuevo cliente")
            clavefe   = input("Escriba la clave  del nuevo cliente")
            nuevocliente = Cliente()
            nuevocliente.cedula = cedulafe
            nuevocliente.nombre = nombrefe
            nuevocliente.primerapellido = pafe
            nuevocliente.segundoapellido = safe
            nuevocliente.direccion = direccionfe
            nuevocliente.correoelectronico = correolectronicofe
            nuevocliente.tipo = tipofe
            nuevocliente.clave = clavefe
            nuevocliente.guardar()

        elif opcion == "2":
            nuevocliente = Cliente()
            for elemento in nuevocliente.listar():
                print(elemento.cedula + " " + elemento.nombre)
        elif opcion == "3":
            break
        elif opcion == "4":
            cedulafe = input("Escriba la cedula a eliminar")
            nuevocliente = Cliente()
            nuevocliente.cedula = cedulafe
            nuevocliente.eliminar()
            break
        elif opcion == "5":
            print("De los siguientes clientes escriba la cedula del que quiere modificar")
            nuevocliente = Cliente()
            for elemento in nuevocliente.listar():
                print(elemento.cedula + " " + elemento.nombre)
            cedulafe = input()
            nuevocliente.cedula = cedulafe
            nuevocliente.nombre = input("Escriba el nuevo nombre del cliente")
            nuevocliente.primerapellido = input("Escriba el nuevo primer apellido del cliente")
            nuevocliente.segundoapellido = input("Escriba el nuevo segundo apellido del cliente")
            nuevocliente.direccion = input("Escriba la nueva direccion del cliente")
            nuevocliente.correoelectronico = input("Escriba el nuevo correo del cliente")
            nuevocliente.tipo = input("Escriba el nuevo tipo del cliente")
            nuevocliente.clave = input("Escriba la nueva clave del cliente")

            nuevocliente.modificar()
            break
        else:
            print("Seleccione una opcion correcta")
