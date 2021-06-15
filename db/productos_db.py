from typing import Dict
from pydantic import BaseModel

#Definicion de ProductInDB
class ProductInDB(BaseModel):
    nombre_producto: str
    cantidad: int
    precio_compra: int
    pvp: int
    fecha_vencimiento: str
    #disponibilidad: bool

#DB ficticia
database_productos = Dict[str, ProductInDB]
database_productos = {
    "Pan": ProductInDB(**{"nombre_producto":"Pan",
                                "cantidad":10,
                                "precio_compra":4500,
                                "pvp":5000,
                                "fecha_vencimiento":"2020-12-31"
                                }),
    "Jabon": ProductInDB(**{"nombre_producto":"Jabon",
                                "cantidad":8,
                                "precio_compra":3850,
                                "pvp":4200,
                                "fecha_vencimiento":"2021-03-25"
                                }),   
    "Margarina": ProductInDB(**{"nombre_producto":"Margarina",
                                "cantidad":5,
                                "precio_compra":1300,
                                "pvp":1550,
                                "fecha_vencimiento":"2021-09-13"
                                }), 
    "Jugo": ProductInDB(**{"nombre_producto":"Jugo",
                                "cantidad":6,
                                "precio_compra":1700,
                                "pvp":2000,
                                "fecha_vencimiento":"2021-01-18"
                                }),
    "Huevo": ProductInDB(**{"nombre_producto":"Huevo",
                                "cantidad":30,
                                "precio_compra":290,
                                "pvp":350,
                                "fecha_vencimiento":"2020-12-18"
                                }),
    "Agua": ProductInDB(**{"nombre_producto":"Agua",
                                "cantidad": 12,
                                "precio_compra":1450,
                                "pvp":1600,
                                "fecha_vencimiento":"2021-12-12"
                                }),
    "Arroz": ProductInDB(**{"nombre_producto":"Arroz",
                                "cantidad": 20,
                                "precio_compra":1350,
                                "pvp":1590,
                                "fecha_vencimiento":"2021-10-02"
                                }),                             
}

#Definicion de funciones de la base de datos
#Obtener la informacion del producto
def get_producto(nombre_producto: str):
    if nombre_producto in database_productos.keys():
        return database_productos[nombre_producto]
    else:
        return None

#Actualizar la informacion del producto en la base de datos
def update_producto(producto_in_db: ProductInDB):
    database_productos[producto_in_db.nombre_producto] = producto_in_db
    return producto_in_db

#Busca productos por nombre dentro de la base de datos
def busca_nombre(nombre_producto: str):
    for obj in database_productos.values():
        if "nombre_producto" in obj.dict() and obj.nombre_producto == nombre_producto:
            return obj
