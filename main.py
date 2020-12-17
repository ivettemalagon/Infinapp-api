from db.productos_db import ProductInDB
from db.productos_db import update_producto, get_producto, busca_nombre

from models.productos_models import SeeProduct, UpdateProduct

from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()

#Funcionalidad get_producto:
@api.get("/inventory/product/{nombre_producto}")
async def buscar_producto(nombre_producto: str):
    producto_in_db = get_producto(nombre_producto)
    existe = busca_nombre(producto_in_db)
    if (producto_in_db == None) or (existe == producto_in_db):
        raise HTTPException(status_code=404, detail="El producto no se encuentra en el inventario")
    product_out = SeeProduct(**producto_in_db.dict())
    return product_out

#Funcionalidad  update_product:
@api.put("/inventory/product/modify/{nombre_producto}")
async def modificar_producto(producto_in_db: ProductInDB):
    producto_db = get_producto(producto_in_db.nombre_producto)
    new_cant = producto_in_db.cantidad
    new_precio = producto_in_db.precio_compra
    new_pvp = producto_in_db.pvp
    new_ven = producto_in_db.fecha_vencimiento
    if producto_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no se encuentra en el inventario")
    if producto_db.cantidad != new_cant:
        producto_db.cantidad = new_cant
    if producto_db.precio_compra != new_precio:
        producto_db.precio_compra = new_precio
    if producto_db.pvp != new_pvp:
        producto_db.pvp = new_pvp
    if producto_db.fecha_vencimiento != new_ven:
        producto_db.fecha_vencimiento = new_ven
    product_out = UpdateProduct(**producto_db.dict())
    return product_out