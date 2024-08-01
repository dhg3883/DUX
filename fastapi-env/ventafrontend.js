class venta{
    constructor( 
        id,
        fecha,
        cliente,
        productos,
        montototal,
        impuesto,
        montototalconimpuesto
    )
    {
        this.id = id,
        this.fecha = fecha,
        this.cliente = cliente,
        this.productos = productos,
        this.montototal = montototal,
        this.impuesto = impuesto,
        this.montototalconimpuesto = montototalconimpuesto
        
    }
    
      Guardar()
            {
                var objetoaenviar = this;
                
                return new Promise(function(resolve,reject)
                                  
                                  {
                    try
                        
                        {
                            var xhr = new XMLHttpRequest();
                            xhr.open('PUT','/ventas');
                            xhr.setRequestHeader('Content-Type','application/json');
                            xhr.onload = function(){
                                if(xhr.status == 200)
                                    {
                                        resolve(JSON.parse(xhr.responseText));
                                    }
                                else
                                    {
                                        reject(xhr);
                                    }
                            };
                            xhr.send(JSON.stringify(objetoaenviar));
                        }
                        catch(err)
                            {
                                reject(err.message);
                            }
                }
                                  );
            }
      
    
    
}