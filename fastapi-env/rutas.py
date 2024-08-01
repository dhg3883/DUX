from Producto import *
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi import Request
from typing import Annotated
from typing import Any, Dict, AnyStr, List, Union
import json
from fastapi import Body, FastAPI


app= FastAPI()


JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]



@app.get("/clienteingresa")
async def root():
    return FileResponse('Cliente.html')


@app.get("/clientejs")
async def root():
    return FileResponse('clientefrontend.js')



@app.put("/clientes")
async def root():
    return FileResponse('clientefrontend.js')




@app.put("/clientes")
async def main(request: Request): 
    return await dict(request.headers.items())


