from Producto import *
from Cliente import *
from venta import *
from datetime import date

def generamenuVenta():
    ventaactual = venta()
    clienteactual = Cliente()
    while True:
        print("Presiona 1 para guardar un nuevo producto")
        print("Presiona 2 para listar los productos guardados")
        print("Presiona 3 Salir")

        opcion = input()

        if opcion == "1":
            print("Primero debes ingresar al sistema como cliente")
            correo =   input("Escriba el correo de cliente")
            clave = input("Escriba la clave de cliente")
            nuevocliente = Cliente()
            nuevocliente.correolectronico = correo
            nuevocliente.clave = clave
            clienteactual = nuevocliente.login()
            if clienteactual.cedula != "-1":
                ventaactual.cliente = clienteactual
                print("Ya esta ingresado, a continuacion vera los productos disponibles")
                nuevoproducto = producto()
                for elemento in nuevoproducto.listar():
                    print(elemento.id + " " + elemento.nombre)
            while True:
                nuevoproducto = producto()
                for elemento in nuevoproducto.listar():
                    print(elemento.id + "-" + elemento.nombre)
                print("Escoja el identificador del producto a comprar o escriba Salir")
                op = input()
                nuevoproducto = producto()
                for elemento in nuevoproducto.listar():
                    if(op == elemento.id):
                        productito = producto()
                        productito.id = opcion
                        productito = productito.productoxid()
                        ventaactual.productos.append(productito)
                        ventaactual.fecha = str( date.today())
                        ventaactual.id= input("Escriba un numero identificador unico de la venta")
                        ventaactual.impuesto = float(input("Escriba el impuesto de la venta"))
                        ventaactual.montototal = ventaactual.calculaMontoTotalsinimp()
                        print("Monto Total de la venta sin impuesto: " + str(ventaactual.montototal))
                        ventaactual.montototalconimpuesto = ventaactual.calculaMontoTotalconimp()
                        print("Monto Total de la venta con impuesto: " + str(ventaactual.montototalconimpuesto))
                        ventaactual.guardar()
                        print("Venta realizada")
                        generamenuVenta( )
                    if(opcion == "Salir"):
                        break
            else:
                break

        elif opcion == "2":
            nuevatienda = venta()
            nuevoproducto = producto()
            for elemento in nuevatienda.listar():
                print(elemento.id+","+elemento.fecha +",")
                for element in nuevatienda.productos:
                        print(element.nombre)


 