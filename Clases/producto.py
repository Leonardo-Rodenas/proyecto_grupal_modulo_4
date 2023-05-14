from proveedor import Proveedor

# clase Producto con sus atributos y métodos
class Producto():
    # La Clase Producto deberá contar con los siguientes atributos: SKU, Nombre, Categoría, Proveedor, Stock, Valor_Neto e __Impuesto = 1.19
    sku:int
    nombre:str 
    categoria:str 
    proveedor:Proveedor 
    stock:int 
    valor_neto:int 
    __impuesto:int = 0.19

    def __init__(self, sku, nombre, proveedor, stock, valor_neto, categoria = "Sin categorizar"):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto

    def __str__(self):
        print(f"El stock del producto {self.nombre} es de {self.stock}")
        return f"{self.nombre}: {self.stock}"
    
    def agregar_stock(self, cantidad):
        self.stock += cantidad
        print(self.stock)

    # Como se encuentra trabajando en el desarrollo del módulo de Python Básico, se solicita integrar correctamente los métodos de las clases.
    def valor_bruto(self):
        return self.valor_neto + (self.valor_neto * self.__impuesto)
    
    def actualizar_stock(self, stock):
        self.stock += stock
        print(self.stock)

    def unidades_disponibles(self):
        return self.stock