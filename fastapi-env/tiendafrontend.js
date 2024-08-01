class tienda{
    constructor( 
        id,
        nombre,
        descripcion,
        direccion,
        telefonos
    )
    {
        this.id = id,
        this.nombre=nombre,
        this.descripcion=descripcion,
        this.direccion = direccion,
        this.telefonos= telefonos
       
    }
    
      Guardar()
            {
                var objetoaenviar = this;
                
                return new Promise(function(resolve,reject)
                                  
                                  {
                    try
                        
                        {
                            var xhr = new XMLHttpRequest();
                            xhr.open('PUT','/tiendas');
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
       Modificar()
            {
                var objetoaenviar = this;
                
                return new Promise(function(resolve,reject)
                                  
                                  {
                    try
                        
                        {
                            var xhr = new XMLHttpRequest();
                            xhr.open('POST','/tiendas');
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
      Eliminar()
            {
                var objetoaenviar = this;
                
                return new Promise(function(resolve,reject)
                                  
                                  {
                    try
                        
                        {
                            var xhr = new XMLHttpRequest();
                            xhr.open('DELETE','/tiendas');
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
     Seleccionartodos()
            {
                var objetoaenviar = this;
                
                return new Promise(function(resolve,reject)
                                  
                                  {
                    try
                        
                        {
                            var xhr = new XMLHttpRequest();
                            xhr.open('GET','/tiendas');
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