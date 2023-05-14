from producto import Producto
from proveedor import proveedor1, proveedor2, proveedor3, proveedor4, proveedor5

# Definir la clase Bodega que maneja los productos
class Bodega:
    def __init__(self, nombre = "Bodega Default"):
        self.nombre = nombre
        self.productos = [
            Producto("123546", "ZAPATILLAS", proveedor1, 20, 3500, "Deportes"),
            Producto("465789", "POLERAS", proveedor2, 10, 3000),
            Producto("456789", "ZAPATOS", proveedor2, 15, 45000, "Zapateria"),
            Producto("159783","POLERÓN", proveedor3, 3, 25000),
            Producto("125678", "CHAQUETA", proveedor4, 5, 7500, "Moda"),
            Producto("142596", "GUANTES", proveedor5, 4, 5650)
        ]

    def agregar_producto(self, sku, nombre, proveedor, stock, valor_neto, categoria=None):
        self.productos.append(Producto(sku, nombre, categoria, proveedor, stock, valor_neto))

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.stock > 0:
                return producto
        return None

    def unidades_disponibles(self):
        return [str(producto) for producto in self.productos]

    def unidades_disponibles_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto:
            return str(producto)
        else:
            return f"{nombre} no encontrado."

    def productos_con_mas_de_n_unidades(self, n):
        return [str(producto) for producto in self.productos if producto.stock > n]