from Clases.proveedor import Proveedor
from Clases.bodega import Bodega, proveedor1, proveedor2, proveedor3, proveedor4, proveedor5
from Clases.sucursal import Sucursal
from Clases.venta import Ventas
from Clases.cliente import Cliente  
from Clases.producto import Producto
from Clases.vendedor import Vendedor
from Clases.orden_compra import OrdenCompra


#instancias y pruebas de métodos en sucursal
sucursal1 = Sucursal("1346789", "Sucursal 1", "Calle 1", 1234567, "sucursal_correo@example.com", 49)
sucursal2 = Sucursal("1346789", "Sucursal 1", "Calle 1", 1234567, "sucursal_correo@example.com", 50)
sucursal3 = Sucursal("1346789", "Sucursal 1", "Calle 1", 1234567, "sucursal_correo@example.com", 70)
sucursal1.__str__()
sucursal1.solicitar_productos()
sucursal1.reponer_productos()
sucursal2.__str__()
sucursal2.solicitar_productos()
sucursal2.reponer_productos()
sucursal3.__str__()
sucursal3.solicitar_productos()
sucursal3.reponer_productos()

bodega = Bodega()

# Agregar productos a la bodega
bodega.agregar_producto("123546", "ZAPATILLAS", proveedor1, 20, 3500, "Deportes")
bodega.agregar_producto("465789", "POLERAS", proveedor2, 10, 3000)
bodega.agregar_producto("456789", "ZAPATOS", proveedor2, 15, 45000, "Zapateria")
bodega.agregar_producto("159783","POLERÓN", proveedor3, 3, 25000)
bodega.agregar_producto("125678", "CHAQUETA", proveedor4, 5, 7500, "Moda")
bodega.agregar_producto("142596", "GUANTES", proveedor5, 4, 5650)

# Crear objeto ventas
ventas = Ventas()

# Agregar clientes
ventas.agregar_cliente(12346587, "Pedrito", "Pascal", "mandaloriano_grogu@gmail.com", "05/03/2019", 250000)
ventas.agregar_cliente(1472589, "Elizabeth", "Erazo", "eli_era2023@gmail.com", "24/09/2022", 170000)

# Realizar ventas de ejemplo
print("\n" + "Ventas de ejemplo")
print(ventas.solicitar_compra(12346587, "Zapatillas", 5))
print(ventas.solicitar_compra(12346587, "Chaqueta", 1))
print(ventas.solicitar_compra(1472589, "Zapatos", 3))
print(ventas.solicitar_compra(1472589, "Polerón", 2))

# Verificar si existe stock necesario y autorizar las compras
print("\nVerificar stock de ejemplo")
print(ventas.autorizar_compra("Zapatillas", 25)) # Se simula compra que sobrepasa el stock = Compra cancelada
print(ventas.autorizar_compra("Chaqueta", 1))
print(ventas.autorizar_compra("Zapatos", 3))
print(ventas.autorizar_compra("Polerón", 2))

# Imprimir el número de clientes
print("\nNúmero de clientes registrados:", ventas.numero_de_clientes())


# Desarrollar 5 instancias de cada clase creada en los puntos anteriores.
cliente1 = Cliente(123, "Juan", "Perez","correo1@gmail.com", 20000, "04/05/2021")
cliente2 = Cliente(789, "Pedrito", "Pascal","correo2@gmail.com", 60000)
cliente3 = Cliente(147, "María", "Gómez","correo3@gmail.com", 200000)
cliente4 = Cliente(369, "Dwayne", "Jhonson","the_rock_is_cooking@gmail.com", 38000, "14/05/2019")
cliente5 = Cliente(159, "Pablo", "Escobar","king_of_drugs@gmail.com", 150000, "25/10/2019")

producto1 = Producto(123456789, "Zapatilla","TeLoVendo", 10, 3000)
producto2 = Producto(789456132, "Chaqueta", "TeLoVendo", 5, 7500)
producto3 = Producto(147258369, "Zapatos", "TeLoVendo", 15, 4500, "Zapateria")
producto4 = Producto(369258147, "Polerón","TeLoVendo", 3, 2500)
producto5 = Producto(1597531496, "Guantes", "TeLoVendo", 4, 5650)

print()
producto1.__str__()
producto1.actualizar_stock(50)
producto1.actualizar_stock(20)


vendedor1 = Vendedor("17.125.489-k", "Manuel", "Gutierrez", "Chaqueta")
vendedor2 = Vendedor("13.213.489-5", "Sofía", "Perez", "Zapatillas")
vendedor3 = Vendedor("12.147.789-6", "Elizabeth", "Erazo", "Guantes")
vendedor4 = Vendedor("16.236.478-5", "Karen", "Smith", "Zapatos")
vendedor5 = Vendedor("10.456.147-k", "Carlos", "Pacheco", "Polerón")

vendedor1.hacer_oferta("zapatilla", 3500)
print()
print("El saldo del cliente: " + cliente1.nombre + " es $" + str(int(cliente1.obtener_saldo())))
print("El saldo del cliente: " + cliente2.nombre + " es $" + str(int(cliente2.obtener_saldo())))
print("El saldo del cliente: " + cliente3.nombre + " es $" + str(int(cliente3.obtener_saldo())))
print("La cliente: " + cliente4.nombre + ", tiene un nuevo saldo de $" + str(cliente4.agregar_saldo(1500)))
print("El cliente: " + cliente5.nombre + ", tiene un nuevo saldo de $" + str(cliente5.agregar_saldo(600)) + "\n")
print("El valor bruto del producto: " + producto1.nombre + " es de $" + str(int(producto1.valor_bruto())))
print("El valor bruto del producto: " + producto2.nombre + " es de $" + str(int(producto2.valor_bruto())))
print("El valor bruto del producto: " + producto3.nombre + " es de $" + str(int(producto3.valor_bruto())))
print("El valor bruto del producto: " + producto4.nombre + " es de $" + str(int(producto4.valor_bruto())))
print("El valor bruto del producto: " + producto5.nombre + " es de $" + str(int(producto5.valor_bruto())) + "\n")
print("El vendedor - Run:"+ vendedor1.run + ", " + vendedor1.nombre + " " + vendedor1.apellido + " tiene una comisión extra de: " + str(int(vendedor1.calcular_comision(45000))))
print("La vendedora - Run:"+ vendedor2.run + ", " + vendedor2.nombre + " " + vendedor2.apellido + " tiene una comisión extra de: " + str(int(vendedor2.calcular_comision(25000))))
print("La vendedora - Run:"+ vendedor3.run + ", " + vendedor3.nombre + " " + vendedor3.apellido + " tiene una comisión extra de: " + str(int(vendedor3.calcular_comision(7500))))
print("La vendedora - Run:"+ vendedor4.run + ", " + vendedor4.nombre + " " + vendedor4.apellido + " tiene una comisión extra de: " + str(int(vendedor4.calcular_comision(25000))))
print("El vendedor - Run:"+ vendedor5.run + ", " + vendedor5.nombre + " " + vendedor5.apellido + " tiene una comisión extra de: " + str(int(vendedor5.calcular_comision(3000))) + "\n")
                        
print(cliente1.obtener_saldo())
vendedor2.vender(producto3, cliente1)    

#Instancias de clase proveedor y prueba de sus métodos
proveedor1 = Proveedor("55.210.101-1", "Adidas Chile S.A.", "Adidas", True)
proveedor2 = Proveedor("72.159.101-8", "Alibaba Ltda.", "Alibaba", True, "China")
proveedor3 = Proveedor("72.258.146-7", "Everlast S.A.", "Everlast", True, "USA")
proveedor4 = Proveedor("15.063.978-5", "Tomás Leiva E.I.R.L.", "Tómas Shop", True, "Chile")
proveedor5 = Proveedor("13.486.45", "Eduardo Carrasco S.A.", "Edo Store", True, "Chile")
proveedor1.juridica_o_natural()
proveedor1.solicitar_firma_documentos("Juan Perez", "Adidas", 55)
cliente3.solicitar_tarjeta()
cliente5.solicitar_entrega()

producto1 = Producto("12364", "Zapatilla", "TeLoVendo", 10, 25000)
orden_compra1 = OrdenCompra(1, producto1, True)
orden_compra1.calcular_total(15000)

