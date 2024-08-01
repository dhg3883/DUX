from Persona import *
import os.path


class Cliente(Persona):
    tipo= ""
    clave = ""
    def guardar(self):
         bandera = True
         with open("Cliente.txt", "a+") as myfile:
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
                    
                        if(self.cedula == sublista[0]):
                            print("Cedula ingresada ya existe en nuestros registros")
                            bandera= False
                            break
                        else:
                            self.cedula = sublista[0]
                            self.nombre = sublista[1]
                            self.primerapellido= sublista[2]
                            self.segundoapellido = sublista[3]
                            self.direccion= sublista[4]
                            self.correolectronico= sublista[5]
                            self.tipo= sublista[6]
                            self.clave = sublista[7]
                    
                    except Exception:
                        pass
         if bandera:
             file_name = 'Cliente.txt'#cargamos el archivo de texto en una variable
             with open(file_name, 'a') as x_file:
                    x_file.write(self.cedula + '*' + self.nombre + '*' + self.primerapellido + '*' + self.segundoapellido + '*' + self.direccion + '*' + self.correoelectronico + '*' + self.tipo +'*' + self.clave +'>')
             print("Dato Guardado correctamente")
             
         
            #en la liena anterior le guardamos al archivo de texto ademas de lo que ya tiene una nueva linea de texto, notese que para separar
            #cada campo de la categoria le agregamos un '*', y al final agregamos un '@', para decir que ahi termina el objeto

    def listar(self):
           
           with open("Cliente.txt", "r") as myfile:

            data = myfile.readlines()
            #el archivo de texto guarda los clientes sin formato, es decir en texto puro, entonces separamos los datos con caracteres comodines
            #, cada objeto tipo categoria guardado en el texto, tendra al final un carcater '@', para saber que estamos ante un nuevo objeto
            #y dentro de cada objeto se separa cada campo del mismo por un caracter '*', el orden siempre del guardado es:nombre,descripcion,identificacion
            #en la siguiente linea, creamos una lista de cadenas de texto, pero ya separando cada objeto tipo categoria
            if(len(data) > 0):

                ft = data[0].split('>')
                listadeclientes=[]
                for elemento in ft:  # iteramos cada elemento en la lista
                    try:  # este comando evita que se caiga en sistema si hay errores
                        sublista = elemento.split('*')  # creamos una nueva lista por cada objeto de la lista anterior, esta vez separandola por el campo
                    
                   
                        nuevocliente = Cliente()
                        nuevocliente.cedula = sublista[0]
                        nuevocliente.nombre = sublista[1]
                        nuevocliente.primerapellido= sublista[2]
                        nuevocliente.segundoapellido = sublista[3]
                        nuevocliente.direccion= sublista[4]
                        nuevocliente.correolectronico= sublista[5]
                        nuevocliente.tipo= sublista[6]
                        nuevocliente.clave = sublista[7]
                        listadeclientes.append(nuevocliente)
                    except Exception:
                        pass
            return listadeclientes
    def login(self):
           if(self.correolectronico != "" and self.clave != ""):
               nuevocliente = Cliente()
               nuevocliente.cedula = "-1"
               with open("Cliente.txt", "r") as myfile:

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
                            if(len(sublista) > 1):
                                nuevocliente.cedula = sublista[0]
                                nuevocliente.nombre = sublista[1]
                                nuevocliente.primerapellido= sublista[2]
                                nuevocliente.segundoapellido = sublista[3]
                                nuevocliente.direccion= sublista[4]
                                nuevocliente.correolectronico= sublista[5]
                                nuevocliente.tipo= sublista[6]
                                nuevocliente.clave = sublista[7]
                        
                                if (self.correolectronico == nuevocliente.correolectronico and self.clave == nuevocliente.clave):
                                    break
                                else:
                                    nuevocliente.cedula = "-1"
                        

                        except Exception:
                            pass
                return nuevocliente
           else:
                print("Escriba el correo y la clave")
    def rellenaarchivoconlalista(self,lista):
        datosentexto=""
        for elemento in lista:
            datosentexto +=  elemento.cedula + '*' + elemento.nombre + '*' + elemento.primerapellido + '*' + elemento.segundoapellido + '*' + elemento.direccion + '*' + elemento.correolectronico + '*' + elemento.tipo +'*' + elemento.clave +'>'
        file_name = 'Cliente.txt'#cargamos el archivo de texto en una variable
        with open(file_name, 'w') as x_file:
            x_file.write(datosentexto)
    
            

    def eliminar(self):
           listadeclientes=[]
           if(self.cedula != "" ):
               with open("Cliente.txt", "r") as myfile:

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
                            if(len(sublista) > 1):
                                nuevocliente = Cliente()
                                nuevocliente.cedula = sublista[0]
                                nuevocliente.nombre = sublista[1]
                                nuevocliente.primerapellido= sublista[2]
                                nuevocliente.segundoapellido = sublista[3]
                                nuevocliente.direccion= sublista[4]
                                nuevocliente.correolectronico= sublista[5]
                                nuevocliente.tipo= sublista[6]
                                nuevocliente.clave = sublista[7]
                                listadeclientes.append(nuevocliente)
                        except Exception:
                            pass
                    for dato in listadeclientes:
                        if(self.cedula == dato.cedula):
                            listadeclientes.remove(dato)
                    self.rellenaarchivoconlalista(listadeclientes)
                    print("Cliente con cedula: " + self.cedula + " ha sido eliminado")
                    return listadeclientes
                
           else:
                print("Escriba la cedula a eliminar")
    def modificar(self):
           listadeclientes=[]
           if(self.cedula != "" ):
               with open("Cliente.txt", "r") as myfile:

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
                            if(len(sublista) > 1):
                                nuevocliente = Cliente()
                                nuevocliente.cedula = sublista[0]
                                nuevocliente.nombre = sublista[1]
                                nuevocliente.primerapellido= sublista[2]
                                nuevocliente.segundoapellido = sublista[3]
                                nuevocliente.direccion= sublista[4]
                                nuevocliente.correolectronico= sublista[5]
                                nuevocliente.tipo= sublista[6]
                                nuevocliente.clave = sublista[7]
                                listadeclientes.append(nuevocliente)
                        except Exception:
                            pass
                    for dato in listadeclientes:
                        if(self.cedula == dato.cedula):
                            listadeclientes.remove(dato)
                            dato.cedula = self.cedula 
                            dato.nombre=self.nombre 
                            dato.primerapellido= self.primerapellido
                            dato.segundoapellido = self.segundoapellido
                            dato.direccion=self.direccion
                            dato.correolectronico= self.correolectronico
                            dato.tipo= self.tipo
                            dato.clave = self.clave
                            listadeclientes.append(dato)
                    self.rellenaarchivoconlalista(listadeclientes)
                    print("Cliente con cedula: " + self.cedula + " ha sido actualizado")
                    return listadeclientes
                
           else:
                print("Escriba la cedula a eliminar")
