# clase Cliente con su atributo y método
    # Se debe crear métodos en la clase Cliente, lo cual puedan agregar y mostrar saldo.
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