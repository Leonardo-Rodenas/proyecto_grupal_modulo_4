import random
# DESARROLLO - Continuación del trabajo.

# Definir la clase Cliente con su atributo y método
class Cliente():
    # La Clase Cliente deberá contar con los siguientes atributos: ID Cliente, Nombre, Apellido, Correo, Fecha Registro y __Saldo
    id_cliente:int
    nombre:str
    apellido:str 
    correo:str 
    fecha_registro:str 
    __saldo:int
    tiene_tarjeta:bool = False

    def __init__(self, id_cliente, nombre, apellido, correo, saldo, fecha_registro = None):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.__saldo = saldo
        self.fecha_registro = fecha_registro

    # Se debe crear métodos en la clase Cliente, lo cual puedan agregar y mostrar saldo.
    def obtener_saldo(self):
        return self.__saldo
    
    def agregar_saldo(self, saldo):
        self.__saldo = self.__saldo + saldo
        return self.__saldo

    def pagar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"El cliente pagó ${int(valor)}. Saldo restante: ${int(self.__saldo)}")
        else:
            print(f"No hay suficiente saldo para realizar el pago de ${valor}. Saldo disponible: ${self.__saldo}")

    def solicitar_tarjeta(self):

        if self.tiene_tarjeta:
            print("Ya tienes una tarjeta")
            return 
        direccion = input("Ingresa tu dirección para enviar la tarjeta: ")
        while not direccion:
            direccion = input("Por favor, ingresa una dirección válida: ")
        identificacion = input("Ingresa tu número de identificación (ej. RUT): ")
        while not identificacion:
            identificacion = input("Por favor, ingresa un número de identificación válido: ")
        print("Procesando solicitud de tarjeta para el cliente", self.nombre, self.apellido, "con identificación", identificacion)
        print("La tarjeta será enviada a la dirección", direccion)
        self.tiene_tarjeta = True

    def solicitar_entrega(self):
        print(f"Bienvenido {self.nombre}, ¿desea entrega en tienda o despacho?")
        opcion = input("Ingrese T para entrega en tienda o D para despacho: ").lower()
        
        while opcion not in ["t", "d"]:
            opcion = input("Ingrese una opción válida (T o D): ").lower()
            
        if opcion == "t":
            print("La entrega se realizará en tienda")
        else:
            direccion = input("Ingresa la dirección de entrega: ")
            correo = input("Ingresa el correo electrónico de contacto: ")    
            print(f"La entrega se realizará en la dirección {direccion} y el correo de contacto es {correo}")

# Definir la clase Proveedor con sus atributos y métodos
class Proveedor:
    rut: str
    nombre_legal: str
    razon_social: str
    pais: str
    persona_juridica: bool = True

    def __init__(self, rut, nombre_legal, razon_social, persona_juridica, pais = None):
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.persona_juridica = persona_juridica

    def juridica_o_natural(self):
        rut = input("Por favor ingrese su rut:")
        rut = rut.replace(".", "").replace("-", "").upper()       
        rut = rut[0:-1] 
        if int(rut) >= 40000000:
            print("El rut ingresado corresponde a una persona jurídica")
        else:
            print("El rut ingresado corresponde a una persona natural")

    def solicitar_firma_documentos(self, razon_social, *args):
        if len(args) == 1:
            self.nombre_legal = args[0]
        if len(args) == 2:
            self.nombre_legal = args[0]
            self.cantidad_provista = args[1]
        if len(args) == 3:
            self.nombre_legal = args[0]
            self.cantidad_provista = args[1]
            self.rut = args[2]
        print(f"Por favor, representante de la empresa {razon_social}, valide los datos y firme para confirmar la entrega de productos.")
        print("Nombre proveedor: " + self.nombre_legal)
        print("Cantidad Provista entrega: " + str(self.cantidad_provista))
        print("Rut Proveedor: " + self.rut)
        respuesta = input("¿Desea firmar los documentos? (s/n): ")
        if respuesta == "s":
            print("Datos validados. Documentos firmados correctamente.\n")
        else:
            print("Datos no válidos. No se ha firmado la documentación.\n")

#Instancias de clase proveedor y prueba de sus métodos
proveedor1 = Proveedor("55.210.101-1", "Adidas Chile S.A.", "Adidas", True)
proveedor2 = Proveedor("72.159.101-8", "Alibaba Ltda.", "Alibaba", True, "China")
proveedor3 = Proveedor("72.258.146-7", "Everlast S.A.", "Everlast", True, "USA")
proveedor4 = Proveedor("15.063.978-5", "Tomás Leiva E.I.R.L.", "Tómas Shop", True, "Chile")
proveedor5 = Proveedor("13.486.45", "Eduardo Carrasco S.A.", "Edo Store", True, "Chile")
proveedor1.juridica_o_natural()

# Definir la clase Producto con sus atributos y métodos
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
    
    # Se deberá crear un método vender de la clase Vendedor
    # Descontar el valor del producto del stock
    # Calcular el valor final del producto y descontarlo del saldo del cliente
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
            Producto("142596", "GUANTES", proveedor5, 4, 5650),
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
       
# Crear la bodega virtual
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

proveedor1.solicitar_firma_documentos("Juan Perez", "Adidas", 55)
cliente3.solicitar_tarjeta()
cliente5.solicitar_entrega()