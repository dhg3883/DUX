from Tienda import *

def generamenuTienda():
    while True:

  
        print("Presiona 1 para guardar un nueva tienda")
        print("Presiona 2 para listar las tiendas guardadas")
        print("Presiona 3 Salir")

        opcion = input()

        if opcion == "1":
            idfe = input("Escriba el id de la nueva tienda")
            nombrefe = input("Escriba el nombre de la nueva tienda")
            descfe = input("Escriba la descripcion de la nueva tienda")
            direccionfe = input("Escriba la direccion de la nueva tienda")
            telefonosfe = input("Escriba los telefonos de la nueva tienda")
         
            nuevatienda = Tienda()
            nuevatienda.id = idfe
            nuevatienda.nombre = nombrefe
            nuevatienda.descripcion = descfe
            nuevatienda.direccion = direccionfe
            nuevatienda.telefonod = telefonosfe
    
            nuevatienda.guardar()
        elif opcion == "2":
            nuevatienda = Tienda()
            for elemento in nuevatienda.listar():
                print(elemento.id + " " + elemento.nombre)
        elif opcion == "3":
            break
        else:
            print("Seleccione una opcion correcta")