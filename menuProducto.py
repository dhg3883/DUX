from Tienda import *
from Producto import *

def generamenuProducto():
    while True:

  
        print("Presiona 1 para guardar un nuevo producto")
        print("Presiona 2 para listar los productos guardados")
        print("Presiona 3 Salir")

        opcion = input()

        if opcion == "1":
            idfe = input("Escriba el id del nuevo producto")
            nombrefe = input("Escriba el nombre del nuevo producto")
            precioxunidadfe = input("Escriba el precio por unidad del producto")
            unidaddemedidafe = input("Escriba la  unidad de medida del producto")

            print("De las siguientes tiendas, escriba el identificador de la tienda asociada al producto")
            tiendita = Tienda()
            for elemento in tiendita.listar():
                print(elemento.id + " " + elemento.nombre)
            
            tiendita.id = input()
            productito = producto()
            productito.id= idfe
            productito.nombre= nombrefe
            productito.precioxunidad= float(precioxunidadfe)
            productito.unidaddemedida = unidaddemedidafe
            productito.tienda= tiendita
            productito.guardar()
        elif opcion == "2":
            nuevatienda = producto()
            for elemento in nuevatienda.listar():
                print(elemento.id + " " + elemento.nombre)
                for element in nuevatienda.descripcion:
                        print(element.descripcion)
        elif opcion == "3":
            break
        elif opcion == "4":
            cedulafe = input("Escriba la cedula a eliminar")
            nuevocliente = producto()
            nuevocliente.id = cedulafe
            nuevocliente.eliminar()
        else:
            print("Seleccione una opcion correcta")