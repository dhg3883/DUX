from Tienda import *
import sqlite3
from Calificar import calificar
class producto():
    def guardar(self):
        print("Guardando")
        con = sqlite3.connect('python.db')
        cur = con.cursor()
        sql = 'INSERT INTO GUIA VALUES (:GUIAID, :TITULO, :PRECIO, :DESCRIPCION, :FECHA, :AUTOR)'
        cur.execute(sql, dict(GUIAID=self.id, TITULO=self.nombre,PRECIO=self.precioxunidad,DESCRIPCION=self.descripcion,FECHA=self.fecha,AUTOR=self.autor))
        con.commit()
        con.close()
    def listar(self):
        con = sqlite3.connect('python.db')
        con
        cur = con.cursor()
        res = cur.execute( 'SELECT * FROM GUIA')
        listadeclientes=[]
        for row in res:
            nuevocliente = producto()
            nuevocliente.id = row[0]
            nuevocliente.nombre = row[1]
            nuevocliente.precioxunidad = row[2]
            nuevocliente.descripcion = row[3]
            nuevocliente.fecha = row[4]
            nuevocliente.autor= row[5]
            listadeclientes.append(nuevocliente)
        return listadeclientes
    def listarcon(self):
        print(self.autor)
        con = sqlite3.connect('python.db')
        con
        cur = con.cursor()
        sql= 'SELECT * FROM GUIA WHERE AUTOR=(:AUTOR)'
        res = cur.execute( sql, dict(AUTOR=self.autor))
        listadeclientes=[]
        for row in res:
            nuevocliente = producto()
            nuevocliente.id = row[0]
            nuevocliente.nombre = row[1]
            nuevocliente.precioxunidad = row[2]
            nuevocliente.descripcion = row[3]
            nuevocliente.fecha = row[4]
            nuevocliente.autor= row[5]
            listadeclientes.append(nuevocliente)
        return listadeclientes
    
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
    def modifica(self):
        print("self")
        con = sqlite3.connect('python.db')
        cur = con.cursor()
        sql= 'UPDATE USUARIO SET GUIAID=(:GUIAID) WHERE ID=(:ID)'
        cur.execute( sql, dict(GUIAID=self.GUIAID, ID=self.ID))
        listadeclientes=[]
        return listadeclientes

    def calificar(self):
           listadeclientes=[]
           if(self.id != "" ):
               with open("Producto.txt", "r") as myfile:

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
                                nuevocliente = producto()
                                nuevocliente.id = sublista[0]
                                nuevocliente.nombre = sublista[1]
                                nuevocliente.descripcion= sublista[2].split(",")
                                nuevocliente.precioxunidad = float(sublista[3])
                                nuevocliente.unidaddemedida = sublista[4]
                                tiendita = Tienda()
                                tiendita.id = sublista[5]
                                nuevocliente.tienda = tiendita
                                listadeclientes.append(nuevocliente)
                        except Exception:
                            pass
                    for dato in listadeclientes:
                        if(self.id == dato.id):
                            listadeclientes.remove(dato)
                            dato.id = self.id 
                            dato.nombre=self.nombre
                            nuevacalficacion = calificar()
                            for datito in nuevacalficacion.listar():
                                if self.id == nuevacalficacion.id: 
                                    dato.descripcion=+datito.descripcion+","
                            dato.precioxunidad = self.precioxunidad
                            dato.unidaddemedida=self.unidaddemedida
                            tiendita = Tienda()
                            dato.tienda.id = self.tienda.id
                            listadeclientes.append(dato)
                    self.rellenaarchivoconlalista(listadeclientes)
                    print("Cliente con cedula: " + self.id + " ha sido actualizado")
                    return listadeclientes
                
           else:
                print("Escriba la cedula a eliminar")
    def rellenaarchivoconlalista(self,lista):
        datosentexto=""
        idsdeproductosseparadosporcoma=""
        for elemento in lista:
            datosentexto +=  elemento.id + '*' + elemento.nombre + '*' +  elemento.descripcion + '*' + str(float(elemento.precioxunidad)) + '*' + elemento.unidaddemedida + '*'+ elemento.tienda.id +'*'+'>'
        file_name = 'Producto.txt'#cargamos el archivo de texto en una variable
        with open(file_name, 'w') as x_file:
            x_file.write(datosentexto)
    def eliminar(self):
           listadeclientes=[]
           if(self.id != "" ):
               with open("Producto.txt", "r") as myfile:

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
                                nuevocliente = producto()
                                nuevocliente.id = sublista[0]
                                nuevocliente.nombre = sublista[1]
                                nuevocliente.descripcion= sublista[2]
                                nuevocliente.precioxunidad = float(sublista[3])
                                nuevocliente.unidaddemedida = sublista[4]
                                tiendita = Tienda()
                                tiendita.id = sublista[5]
                                nuevocliente.tienda = tiendita
                                listadeclientes.append(nuevocliente)
                        except Exception:
                            pass
                    for dato in listadeclientes:
                        if(self.id == dato.id):
                            listadeclientes.remove(dato)
                    self.rellenaarchivoconlalista(listadeclientes)
                    print("Cliente con cedula: " + self.id + " ha sido eliminado")
                    return listadeclientes
                
           else:
                print("Escriba la cedula a eliminar")
    
