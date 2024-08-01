from Cliente import *
from Producto import *

class venta():
    id=""
    fecha=""
    cliente = Cliente()
    productos= []
    montototal= 0.0
    impuesto = 0.0
    montototalconimpuesto = 0.0
    def guardar(self):
         bandera = True
         with open("venta.txt", "a+") as myfile:
            data = myfile.readlines()
            #el archivo de texto guarda las categorias sin formato, es decir en texto puro, entonces separamos los datos con caracteres comodines
            #, cada objeto tipo categoria guardado en el texto, tendra al final un carcater '@', para saber que estamos ante un nuevo objeto
            #y dentro de cada objeto se separa cada campo del mismo por un caracter '*', el orden siempre del guardado es:nombre,descripcion,identificacion
            #en la siguiente linea, creamos una lista de cadenas de texto, pero ya separando cada objeto tipo categoria
            if(len(data) > 0):
                ft = data[0].split('>')
              
                for elemento in ft:  # iteramos cada elemento en la lista
                    try:  # este comando evita que se caiga en sistema si hay errores
                        sublista = elemento.split('*')  # creamos una nueva lista por cada objeto de la lista anterior, esta vez separandola por el campo
                    
                        if(self.id == sublista[0]):
                            print("Id ingresado ya existe en nuestros registros")
                            bandera= False
                            break
                        else:
                            self.id = sublista[0]
                            self.fecha=sublista[1]
                            clientecito = Cliente()
                            clientecito.cedula = sublista[2]
                            self.cliente = clientecito
                            listadeproductos = sublista[3].split(',')
                            for elementoproducto in listadeproductos:
                                productito = producto()
                                productito.id = elementoproducto
                                productito = productito.productoxid()
                                self.productos.append(productito)
                            self.montototal= float(sublista[4])
                            self.impuesto = float(sublista[5])
                            self.montototalconimpuesto = float(sublista[6])

                    except Exception:
                        pass
         if bandera:
             file_name = 'venta.txt'#cargamos el archivo de texto en una variable
             with open(file_name, 'a') as x_file:
                    idsdeproductosseparadosporcoma=""
                    for productito in self.productos:
                        idsdeproductosseparadosporcoma += productito.id + ','

                    x_file.write(self.id + '*' + self.fecha + '*' + self.cliente.cedula + '*' + idsdeproductosseparadosporcoma + '*' + str(self.montototal) + '*' + str(self.impuesto)  +  '*' + str(self.montototalconimpuesto)  +'>')
             print("Dato Guardado correctamente")
             
         
            #en la liena anterior le guardamos al archivo de texto ademas de lo que ya tiene una nueva linea de texto, notese que para separar
            #cada campo de la categoria le agregamos un '*', y al final agregamos un '@', para decir que ahi termina el objeto

    def listar(self):
           
           with open("venta.txt", "r") as myfile:

            data = myfile.readlines()
            #el archivo de texto guarda los clientes sin formato, es decir en texto puro, entonces separamos los datos con caracteres comodines
            #, cada objeto tipo categoria guardado en el texto, tendra al final un carcater '@', para saber que estamos ante un nuevo objeto
            #y dentro de cada objeto se separa cada campo del mismo por un caracter '*', el orden siempre del guardado es:nombre,descripcion,identificacion
            #en la siguiente linea, creamos una lista de cadenas de texto, pero ya separando cada objeto tipo categoria
            if(len(data) > 0):

                ft = data[0].split('>')
                listadeventas=[]
                for elemento in ft:  # iteramos cada elemento en la lista
                    try:  # este comando evita que se caiga en sistema si hay errores
                        sublista = elemento.split('*')  # creamos una nueva lista por cada objeto de la lista anterior, esta vez separandola por el campo
                    
                        ventita = venta()
                        ventita.id = sublista[0]
                        ventita.fecha=sublista[1]
                        clientecito = Cliente()
                        clientecito.cedula = sublista[2]
                        ventita.cliente = clientecito
                        listadeproductos = sublista[3].split(',')
                        for elementoproducto in listadeproductos:
                                productito = producto()
                                productito.id = elementoproducto
                                productito = productito.productoxid()
                                ventita.productos.append(productito)
                        ventita.montototal= float(sublista[4])
                        ventita.impuesto = float(sublista[5])
                        ventita.montototalconimpuesto = float(sublista[6])
                     
                        listadeventas.append(ventita)
                    except Exception:
                        pass
            return listadeventas

    def calculaMontoTotalsinimp(self):
        montototal = 0.0
        for elementoproducto in self.productos:
            montototal += elementoproducto.precioxunidad
        return montototal
    def calculaMontoTotalconimp(self):
        return self.montototal + (self.montototal * (self.impuesto/100))


