from Tienda import *

class producto():
    id=""
    nombre=""
    descripcion = ""
    precioxunidad= 0.0
    unidaddemedida= ""
    tienda= Tienda()
    def guardar(self):
         bandera = True
         with open("Producto.txt", "a+") as myfile:
            data = myfile.readlines()
            #el archivo de texto guarda las categorias sin formato, es decir en texto puro, entonces separamos los datos con caracteres comodines
            #, cada objeto tipo categoria guardado en el texto, tendra al final un carcater '@', para saber que estamos ante un nuevo objeto
            #y dentro de cada objeto se separa cada campo del mismo por un caracter '*', el orden siempre del guardado es:nombre,descripcion,identificacion
            #en la siguiente linea, creamos una lista de cadenas de texto, pero ya separando cada objeto tipo categoria
            if(len(data) > 0):
                ft = data[0].split('>')
                identificadormayor=0
                for elemento in ft:  # iteramos cada elemento en la lista
                    try:  # este comando evita que se caiga en sistema si hay errores
                        sublista = elemento.split('*')  # creamos una nueva lista por cada objeto de la lista anterior, esta vez separandola por el campo
                    
                        if(self.id == sublista[0]):
                            print("Id ingresado ya existe en nuestros registros")
                            bandera= False
                            break
                        else:
                            self.id = sublista[0]
                            self.nombre = sublista[1]
                            self.descripcion= sublista[2]
                            self.precioxunidad = float(sublista[3])
                            self.unidaddemedida= sublista[4]
                            tiendita = Tienda()
                            tiendita.id = sublista[5]
                            self.tienda= tiendita
                    
                    
                    except Exception:
                        pass
         if bandera:
             file_name = 'Producto.txt'#cargamos el archivo de texto en una variable
             with open(file_name, 'a') as x_file:
                    x_file.write(self.id + '*' + self.nombre + '*' + self.descripcion + '*' + str(float(self.precioxunidad)) + '*' + self.unidaddemedida + '*' + self.tienda.id  +'>')
             print("Dato Guardado correctamente")
             
         
            #en la liena anterior le guardamos al archivo de texto ademas de lo que ya tiene una nueva linea de texto, notese que para separar
            #cada campo de la categoria le agregamos un '*', y al final agregamos un '@', para decir que ahi termina el objeto

    def listar(self):
           
           with open("Producto.txt", "r") as myfile:

            data = myfile.readlines()
            #el archivo de texto guarda los clientes sin formato, es decir en texto puro, entonces separamos los datos con caracteres comodines
            #, cada objeto tipo categoria guardado en el texto, tendra al final un carcater '@', para saber que estamos ante un nuevo objeto
            #y dentro de cada objeto se separa cada campo del mismo por un caracter '*', el orden siempre del guardado es:nombre,descripcion,identificacion
            #en la siguiente linea, creamos una lista de cadenas de texto, pero ya separando cada objeto tipo categoria
            if(len(data) > 0):

                ft = data[0].split('>')
                listadetiendas=[]
                for elemento in ft:  # iteramos cada elemento en la lista
                    try:  # este comando evita que se caiga en sistema si hay errores
                        sublista = elemento.split('*')  # creamos una nueva lista por cada objeto de la lista anterior, esta vez separandola por el campo
                    
                   
                        nuevocliente = producto()
                        nuevocliente.id = sublista[0]
                        nuevocliente.nombre = sublista[1]
                        nuevocliente.descripcion= sublista[2]
                        nuevocliente.precioxunidad = float(sublista[3])
                        nuevocliente.unidaddemedida = sublista[4]
                        tiendita = Tienda()
                        tiendita.id = sublista[5]
                        nuevocliente.tienda = tiendita
                     
                        listadetiendas.append(nuevocliente)
                    except Exception:
                        pass
            return listadetiendas

    def productoxid(self):
           nuevocliente = producto()
           with open("Producto.txt", "r") as myfile:
            
            nuevocliente.id=-1
            data = myfile.readlines()
            #el archivo de texto guarda los clientes sin formato, es decir en texto puro, entonces separamos los datos con caracteres comodines
            #, cada objeto tipo categoria guardado en el texto, tendra al final un carcater '@', para saber que estamos ante un nuevo objeto
            #y dentro de cada objeto se separa cada campo del mismo por un caracter '*', el orden siempre del guardado es:nombre,descripcion,identificacion
            #en la siguiente linea, creamos una lista de cadenas de texto, pero ya separando cada objeto tipo categoria
            if(len(data) > 0):

                ft = data[0].split('>')
                
                for elemento in ft:  # iteramos cada elemento en la lista
                    try:  # este comando evita que se caiga en sistema si hay errores
                        sublista = elemento.split('*')  # creamos una nueva lista por cada objeto de la lista anterior, esta vez separandola por el campo
                    
                        if(self.id == sublista[0]):
                            
                            nuevocliente.id = sublista[0]
                            nuevocliente.nombre = sublista[1]
                            nuevocliente.descripcion= sublista[2]
                            nuevocliente.precioxunidad = float(sublista[3])
                            nuevocliente.unidaddemedida = sublista[4]
                            tiendita = Tienda()
                            tiendita.id = sublista[5]
                            nuevocliente.tienda = tiendita
                            break
                     
                        
                    except Exception:
                        pass
            return nuevocliente