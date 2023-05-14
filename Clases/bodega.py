from .producto import Producto
from .proveedor import Proveedor

#Instancias de clase proveedor y prueba de sus métodos
proveedor1 = Proveedor("55.210.101-1", "Adidas Chile S.A.", "Adidas", True)
proveedor2 = Proveedor("72.159.101-8", "Alibaba Ltda.", "Alibaba", True, "China")
proveedor3 = Proveedor("72.258.146-7", "Everlast S.A.", "Everlast", True, "USA")
proveedor4 = Proveedor("15.063.978-5", "Tomás Leiva E.I.R.L.", "Tómas Shop", True, "Chile")
proveedor5 = Proveedor("13.486.45", "Eduardo Carrasco S.A.", "Edo Store", True, "Chile")
proveedor1.juridica_o_natural()

# Definir la clase Bodega que maneja los productos
class Bodega:
    def __init__(self, nombre = "Bodega Default"):
        self.nombre = nombre
        self.productos = [
            Producto("123546", "ZAPATILLAS", proveedor1, 300, 3500, "Deportes"),
            Producto("465789", "POLERAS", proveedor2, 700, 3000),
            Producto("456789", "ZAPATOS", proveedor2, 500, 45000, "Zapateria"),
            Producto("159783","POLERÓN", proveedor3, 600, 25000),
            Producto("125678", "CHAQUETA", proveedor4, 450, 7500, "Moda"),
            Producto("142596", "GUANTES", proveedor5, 290, 5650),
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

bodega = Bodega()

