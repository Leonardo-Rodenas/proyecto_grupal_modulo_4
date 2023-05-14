from .producto import Producto

class OrdenCompra:
  
    id_ordencompra: int
    producto: Producto
    despacho: bool

    def __init__(self, id_ordencompra, producto, despacho):
        self.id_ordencompra = id_ordencompra
        self.producto = producto
        self.despacho = despacho

    def calcular_total(self, precio):
        valor_neto = precio
        impuesto = valor_neto * 0.19  # IVA en Chile
        valor_total = valor_neto + impuesto
        
        if self.despacho == True:
            valor_total += 5000
            print("Detalle de la orden de compra:")
            print(f"Valor neto: {valor_neto}")
            print(f"Impuesto: {impuesto}")
            print("Recargo por despacho: 5000")
            print(f"Valor total: {valor_total}")
        else:
            print("Detalle de la orden de compra:")
            print(f"Valor neto: {valor_neto}")
            print(f"Impuesto: {impuesto}")
            print("Sin recargo por despacho")
            print(f"Valor total: {valor_total}")
