class Cliente{
    
    constructor( 
    ID,
    NOMBRE,
    EMAIL,
    CLAVE,
    GUIAID,
    )
    {
        this.ID= ID;
        this.NOMBRE= NOMBRE;
        this.EMAIL= EMAIL;
        this.CLAVE= CLAVE;
        this.GUIAID=GUIAID;
        
    }
    
      Guardar()
            {

                var objetoaenviar = this;
                
                return new Promise(function(resolve,reject)
                                  
                                  {
                    try
                        
                        {
                            var xhr = new XMLHttpRequest();

                            xhr.open('PUT','/clientes');
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
                console.log(objetoaenviar);
                return new Promise(function(resolve,reject)
                                  
                                  {
                    try
                        
                        {
                            var xhr = new XMLHttpRequest();
                            xhr.open('POST','/clientes');
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
        Login()
            {
                var objetoaenviar = this;
                
                return new Promise(function(resolve,reject)
                                  
                                  {
                    try
                        
                        {
                            var xhr = new XMLHttpRequest();
                            xhr.open('POST','/loginclientes');
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
                            xhr.open('DELETE','/clientes');
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
                            xhr.open('GET','/clientes');
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