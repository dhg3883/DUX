from Producto import *
from Tienda import *
from Calificar import *
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from pydantic import BaseModel
from Cliente import *
from venta import *
app= FastAPI()
class Item(BaseModel):
    ID : str
    NOMBRE : str
    EMAIL : str
    CLAVE : str
    GUIAID: str
class ItemProducto(BaseModel):
    id:str
    nombre:str    
    precioxunidad:str
    descripcion:str
    fecha:str
    autor:str
class ItemCalifica(BaseModel):
    id:str
    descripcion:str
class ItemVenta(BaseModel):
    id:str
    fecha:str
    cliente:str
    productos:str
    montototal:str
    impuesto:str
    montototalconimpuesto :str
class ItemTienda(BaseModel):
    id:str
    nombre : str
    descripcion : str
    direccion : str
    telefonos : str
@app.get("/base")
def root():
    return FileResponse('python.db')
@app.get("/Login")
def root():
    return FileResponse('Login.html')
@app.get("/indicejs")
def root():
    return FileResponse('indice.js')
@app.get("/menu")
def root():
    return FileResponse('Menu.html')
@app.get("/tierra")
def root():
    return FileResponse('./IMG/tierra.png')
@app.get("/ventas")
async def root():
    return FileResponse('venta.html')
@app.get("/estilos")
async def root():
    return FileResponse('estilos.css')
@app.get("/logincss")
async def root():
    return FileResponse('Login.css')

@app.get("/archivopaginaweb")
async def root():
    return FileResponse('Cliente.html')
@app.get("/archivopaginawebproducto")
async def root():
    return FileResponse('Producto.html')

@app.get("/clientejs")
async def root():
    return FileResponse('fastapi-env/clientefrontend.js') 


@app.get("/productojs")
async def root():
    return FileResponse('fastapi-env/productofrontend.js') 

@app.get("/tiendajs")
async def root():
    return FileResponse('fastapi-env/tiendafrontend.js') 
@app.get("/ventajs")
async def root():
    return FileResponse('fastapi-env/ventafrontend.js') 
@app.get("/")
async def root():
    return FileResponse('Indice.html') 
@app.get("/Guias")
async def root():
    return FileResponse('Guias.html') 
@app.get("/indicecss")
async def root():
    return FileResponse('indice.css') 
@app.get("/clientes")
async def root():
    clientecito = Cliente()
    listadeclientesenarchivo = clientecito.listar()
    for elemento in listadeclientesenarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaclienteprimerpaso(\''+ str(elemento.ID) +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminacliente(\''+ str(elemento.ID) +'\')"></input>'
    return listadeclientesenarchivo 
@app.get("/clientes")
async def root():
    clientecito = Cliente()
    listadeclientesenarchivo = clientecito.listar()
    for elemento in listadeclientesenarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaclienteprimerpaso(\''+ str(elemento.ID) +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminacliente(\''+ str(elemento.ID) +'\')"></input>'
    return listadeclientesenarchivo 


@app.get("/tiendas")
async def root():
    tiendita = Tienda()
   
    listadeclientesenarchivo = tiendita.listar()
    for elemento in listadeclientesenarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaenarchivo(\''+ elemento.id +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminacliente(\''+ elemento.id +'\')"></input>'
    return listadeclientesenarchivo 

@app.get("/productos")
async def root():
    tiendita = producto()
    listadeclientesenarchivo = tiendita.listar()
    for elemento in listadeclientesenarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaenarchivo(\''+ str(elemento.id) +'\')"></input>'
    return listadeclientesenarchivo 

@app.post("/productosyu")
async def root(item:ItemProducto):
    clientecito = producto()
    clientecito.id=item.id
    clientecito.nombre=item.nombre
    clientecito.precioxunidad= item.precioxunidad
    clientecito.descripcion = item.descripcion
    clientecito.fecha = item.fecha
    clientecito.autor= item.autor
    listadeclientesenarchivo = clientecito.listarcon()
    for elemento in listadeclientesenarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaenarchivo(\''+ str(elemento.id) +'\')"></input>'
    return listadeclientesenarchivo 

@app.get("/productosparaventa")
async def root():
    tiendita = producto()
   
    listadeclientesenarchivo = tiendita.listar()
    for elemento in listadeclientesenarchivo:
        elemento.tienda = elemento.tienda.id
        elemento.agregar = '<input type="button" value="Agregar" onclick="Agrega(\''+ elemento.id +'\')"></input>'
    return listadeclientesenarchivo 

@app.put("/clientes")
async def root(item:Item):
    clientecito = Cliente()
    clientecito.ID = item.ID
    clientecito.NOMBRE = item.NOMBRE
    clientecito.EMAIL = item.EMAIL
    clientecito.CLAVE = item.CLAVE
    clientecito.GUIAID = item.GUIAID
    clientecito.guardar()
    listadeclientesenarchivo = clientecito.listar()
    for elemento in listadeclientesenarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaclienteprimerpaso(\''+ str(elemento.ID) +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminacliente(\''+ str(elemento.ID) +'\')"></input>'
    return listadeclientesenarchivo

@app.put("/productos")
async def root(item:ItemProducto):
    clientecito = producto()
    clientecito.id=item.id
    clientecito.nombre=item.nombre
    clientecito.precioxunidad= item.precioxunidad
    clientecito.descripcion = item.descripcion
    clientecito.fecha = item.fecha
    clientecito.autor= item.autor
    clientecito.guardar()
    listadeclientesenarchivo = clientecito.listar()
    return listadeclientesenarchivo 
@app.post("/productos")
async def root(item:ItemProducto):
    clientecito = producto()
    clientecito.id=item.id
    clientecito.nombre=item.nombre
    clientecito.descripcion = item.descripcion
    clientecito.precioxunidad= float(item.precioxunidad)
    clientecito.unidaddemedida= item.unidaddemedida
    tiendecita = Tienda()
    tiendecita.id = item.tienda
    clientecito.tienda = tiendecita
    clientecito.calificar()
    listadeclientesenarchivo = clientecito.listar()
    for elemento in listadeclientesenarchivo:
        elemento.tienda = elemento.tienda.id
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaclienteprimerpaso(\''+ elemento.id +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminacliente(\''+ elemento.id +'\')"></input>'
    return listadeclientesenarchivo 
@app.delete("/productos")
async def root(item:ItemProducto):
    clientecito = producto()
    clientecito.id=item.id
    clientecito.nombre=item.nombre
    clientecito.descripcion = item.descripcion
    clientecito.precioxunidad= item.precioxunidad
    clientecito.unidaddemedida= item.unidaddemedida
    tiendecita = Tienda()
    tiendecita.id = item.tienda
    clientecito.tienda = tiendecita
    clientecito.eliminar()
    listadeclientesenarchivo = clientecito.listar()
    for elemento in listadeclientesenarchivo:
        elemento.tienda = elemento.tienda.id
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaclienteprimerpaso(\''+ elemento.id +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminacliente(\''+ elemento.id +'\')"></input>'
    return listadeclientesenarchivo 
@app.post("/calificar")
async def root(item:ItemProducto):
    clientecito = calificar()
    clientecito.id=item.id
    clientecito.descripcion = item.descripcion
    clientecito.calificar()
    listadeclientesenarchivo = clientecito.listar()
    for elemento in listadeclientesenarchivo:
        elemento.modificar = '<input type="button" value="modificar" onclick="modificaclienteprimerpaso(\''+ elemento.id +'\')"></input>'
        elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminacliente(\''+ elemento.id +'\')"></input>'
    return listadeclientesenarchivo 

@app.put("/ventas")
async def root(item:ItemVenta):
    #id=""
    #fecha=""
    #cliente = Cliente()
    #productos= []
    #montototal= 0.0
    #impuesto = 0.0
    #montototalconimpuesto = 0.0
    clientecito = venta()
    clientecito.id=item.id
    clientecito.fecha=item.fecha
    clienteinterno = Cliente()
    clienteinterno.cedula = item.cliente
    clienteinterno.cliente = clienteinterno
    listadeproductosagregados = item.productos.split(',')
    for iteminterno in listadeproductosagregados:
        productointerno = producto()
        productointerno.id = iteminterno
        clientecito.productos.append(productointerno)
    
    clientecito.montototal  = float(item.montototal)
    clientecito.impuesto= float(item.impuesto)
    clientecito.montototalconimpuesto= float(item.montototalconimpuesto)
    clientecito.guardar()
    return "Venta realizada" 

@app.post("/clientes")
async def root(item:Item):
    clientecito = Cliente()
    clientecito.ID = item.ID
    clientecito.NOMBRE = item.NOMBRE
    clientecito.EMAIL = item.EMAIL
    clientecito.CLAVE = item.CLAVE
    clientecito.GUIAID = item.GUIAID
    clientecito.modificar()
    productito = producto()
@app.post("/loginclientes")
async def root(item:Item):
    print("alv")
    clientecito = Cliente()
    clientecito.ID = item.ID
    clientecito.NOMBRE = item.NOMBRE
    clientecito.EMAIL = item.EMAIL
    clientecito.CLAVE = item.CLAVE
    clientecito.GUIAID = item.GUIAID
    return clientecito.login()
@app.delete("/clientes")
async def root(item:Item):
    clientecito = Cliente()
    clientecito.ID = item.ID
    clientecito.NOMBRE = item.NOMBRE
    clientecito.EMAIL = item.EMAIL
    clientecito.CLAVE = item.CLAVE
    clientecito.GUIAID = item.GUIAID
    clientecito.eliminar()
    listadeclientesenarchivo = clientecito.listar()
    for elemento in listadeclientesenarchivo:
       elemento.modificar = '<input type="button" value="modificar" onclick="modificaclienteprimerpaso(\''+ elemento.ID +'\')"></input>'
       elemento.eliminar = '<input type="button" value="eliminar" onclick="eliminacliente(\''+ elemento.ID +'\')"></input>'
    return listadeclientesenarchivo