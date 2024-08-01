from menuClientes import *
from MenuLoginCliente import *
from menuTienda import *
from menuProducto import *
from menuVenta import *
from menuCalificar import *
while True:

    print (30 * "-", "MENU", 30 * "-")
    print ("1. Menu para manejar las Clientes")
    print ("2. Menu para manejar los tiendas")
    print ("3. Menu para manejar los produtos")
    print ("4. Menu para manejar las ventas")
    print ("5. Ingresar como administrador")
    print ("6. Ingresar como cliente")
    print ("7. Una nueva venta")


    opcion = input()

    if opcion == "1":
        generamenu()
    if opcion == "2":
        generamenuTienda()
    elif opcion == "8":
        Menucalificar()
    elif opcion == "6":
        generamenulogin()
    elif opcion == "3":
        generamenuProducto()
    elif opcion == "7":
        generamenuVenta()

