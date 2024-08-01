from Calificar import *
from Producto import *

def Menucalificar():
    while True:

  
        print("Presiona 1 para guardar un nuevo producto")
        print("Presiona 2 para listar los productos guardados")
        print("Presiona 3 Salir")

        opcion = input()

        if opcion == "1":
            idfe = input("Escriba la calificacion del producto")
            print("De las siguientes tiendas, escriba el identificador de la tienda asociada al producto")
            product = producto()
            for elemento in product.listar():
                print(elemento.id + " " + elemento.nombre)
            
            product.id = input()
            for elemento in product.listar():
                if product.id == elemento.id:
                    productito = calificar()
                    productito.descripcion= idfe
                    productito.id = product.id
                    productito.guardar()
                    print("sexo")
                    product.descripcion =productito.id
                    product.calificar()
                else:
                    print("elija bien")
        elif opcion == "2":
            nuevatienda = producto()
            for elemento in nuevatienda.listar():
                print(elemento.nombre + " ")
        elif opcion == "3":
            break
        elif opcion == "4":
            cedulafe = input("Escriba la cedula a eliminar")
            nuevocliente = producto()
            nuevocliente.id = cedulafe
            nuevocliente.eliminar()
        else:
            print("Seleccione una opcion correcta")