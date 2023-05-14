from cliente import Cliente
from abp_ejercicio_grupal_4 import bodega

# Definir la clase Ventas que maneja los clientes y las ventas  
class Ventas:
    def __init__(self, codigo_venta = None):
        self.id_cliente = None
        self.clientes = []
        self.ventas = []
        self.codigo_venta = codigo_venta


    def agregar_cliente(self, id_cliente, nombre, apellido, correo, fecha_registro, saldo):
        self.clientes.append(Cliente(id_cliente, nombre, apellido, correo, fecha_registro, saldo))

    def buscar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None

    def solicitar_compra(self, nombre, nombre_producto, stock=1):
        cliente = self.buscar_cliente(nombre)
        if not cliente:
            return f"Cliente {nombre} no encontrado."
        producto = bodega.buscar_producto(nombre_producto)
        if not producto:
            return f"{nombre_producto} no encontrado en la bodega."
        if producto.stock < stock:
            return f"No hay suficientes unidades de {nombre_producto} en la bodega."
        self.ventas.append((cliente, producto, stock))
        return f"Compra de {stock} unidades de {nombre_producto} realizada por cliente ID = {nombre}."

    def existe_stock_necesario(self, nombre_producto, stock):
        producto = bodega.buscar_producto(nombre_producto)
        if not producto:
            return False
        return producto.stock >= stock

    def autorizar_compra(self, nombre_producto, stock):
        if self.existe_stock_necesario(nombre_producto, stock):
            return "Compra aprobada y en camino"
        else:
            return "Stock insuficiente: Compra cancelada"

    def numero_de_clientes(self):
        return len(self.clientes)