from pydantic import BaseModel

#Modelo para ver la informacion del producto
class SeeProduct(BaseModel):
    nombre_producto: str
    cantidad: int
    precio_compra: int
    pvp: int
    fecha_vencimiento: str

#Modelo para modificar el producto
class UpdateProduct(BaseModel):
    nombre_producto: str
    cantidad: int
    precio_compra: int
    pvp: int
    fecha_vencimiento: str
