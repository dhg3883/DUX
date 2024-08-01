from Persona import *
import sqlite3
import os.path

class Cliente(Persona):
    def guardar(self):
        print("Guardando")
        con = sqlite3.connect('python.db')
        con
        cur = con.cursor()
        cur
        sql = 'INSERT INTO USUARIO VALUES (:ID, :NOMBRE, :EMAIL, :CLAVE, :GUIAID)'
        cur.execute(sql, dict(ID=self.ID, NOMBRE=self.NOMBRE,EMAIL=self.EMAIL,CLAVE=self.CLAVE, GUIAID=[1,2]))

        con.commit()
        con.close()
    def listar(self):
        con = sqlite3.connect('python.db')
        cur = con.cursor()
        res = cur.execute( 'SELECT * FROM USUARIO')
        listadeclientes=[]
        for row in res:
            nuevocliente = Cliente()
            nuevocliente.ID = row[0]
            nuevocliente.NOMBRE = row[1]
            nuevocliente.EMAIL = row[2]
            nuevocliente.CLAVE = row[3]
            nuevocliente.GUIAID= row[4]
            listadeclientes.append(nuevocliente)
        return listadeclientes
    def login(self):
        listadeclientes=[]
        nuevocliente = Cliente()
        if(self.EMAIL != ""):
            con = sqlite3.connect('python.db')
            cur = con.cursor()
            sql= 'SELECT * FROM USUARIO WHERE EMAIL=(:EMAIL) AND CLAVE=(:CLAVE) '
            res = cur.execute( sql, dict(EMAIL=self.EMAIL, CLAVE=self.CLAVE))


            for row in res:
                            if (row != ""):
                                print("verificando")
                                nuevocliente.ID = row[0]
                                nuevocliente.NOMBRE = row[1]
                                nuevocliente.EMAIL = row[2]
                                nuevocliente.CLAVE = row[3]
                                nuevocliente.GUIAID= row[4]
                                listadeclientes.append(nuevocliente)
            return listadeclientes

    
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
        print(self.ID)
        con = sqlite3.connect('python.db')
        cur = con.cursor()
        sql= 'UPDATE USUARIO SET GUIAID = :GUIAID WHERE ID = :ID'
        cur.execute( sql, dict(GUIAID=(self.GUIAID), ID=self.ID))
        listadeclientes=[]
        return listadeclientes
           
