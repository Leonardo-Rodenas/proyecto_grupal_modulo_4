import random
from cliente import Cliente
from producto import Producto

# Creación clase: Vendedor.
class Vendedor:
    # La Clase Vendedor deberá contar con los siguientes atributos: RUN, Nombre, Apellido, Sección y __Comision = 0
    run:str 
    nombre:str 
    apellido:str
    __comision:int
    cliente = Cliente
    seccion:str 
    producto:str

    def __init__(self, run, nombre, apellido, producto, comision = 0.005, seccion = None):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = 0
        self.producto = producto
        self.porcentaje_comision = comision
        
    # Comisión del vendedor
    def calcular_comision(self, venta):
        self.__comision += int(venta * 0.05)
        return self.__comision
    
    def hacer_oferta(self, producto, precio):
        descuento = round(random.uniform(0.05, 0.1) * precio)
        precio_descuento = round(precio - descuento, 2)
        print(f"¡Oferta especial para {producto}! Precio original: ${precio}. Descuento: ${descuento}. Precio con descuento: ${precio_descuento}.")

    def vender(self, producto: Producto, cliente: Cliente):
        if producto.stock == 0:
            print(f"{producto.nombre} no tiene stock disponible. No se ha podido procesar la venta. ")
            return 
        producto.stock -= 1
        comision = int(producto.valor_bruto()*self.porcentaje_comision) 
        self.__comision += comision
        cliente.pagar(producto.valor_bruto())
        print(f"{self.nombre} vendió {producto.nombre}, stock actualizado {producto.stock}")
        print(f"Comisión acumulada: {self.__comision}")
        print(f"Saldo final del cliente: {int(cliente.obtener_saldo())}")