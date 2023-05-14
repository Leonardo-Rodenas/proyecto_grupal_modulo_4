from Clases.bodega import Bodega

class Sucursal:
    id_sucursal:str
    nombre:str
    direccion:str
    telefono:int
    correo:str
    stock: int

    def __init__(self, id_sucursal, nombre, direccion, telefono, correo, stock):
        self.id_sucursal = id_sucursal
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.stock = stock

    def __str__(self):
        return print(f"Stock actual: {self.stock}")

    def solicitar_productos(self):
        if self.stock < 50:
            print("Solicitando y reponiendo productos...")
            self.reponer_productos()
        else:
            print("No es necesario solicitar productos.")

    def reponer_productos(self):
        from .bodega import bodega
        producto = bodega.buscar_producto("BODEGA")
        if producto and producto.stock >= 300:
            self.stock += 300
            producto.stock -= 300
            print(f"Se han repuesto 300 productos. Nuevo stock: {self.stock}")
        else:
            print("No existe suficiente stock en la bodega para reponer.")
