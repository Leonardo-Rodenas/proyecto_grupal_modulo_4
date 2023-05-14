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

# #Instancias de clase proveedor y prueba de sus métodos
# proveedor1 = Proveedor("55.210.101-1", "Adidas Chile S.A.", "Adidas", True)
# proveedor2 = Proveedor("72.159.101-8", "Alibaba Ltda.", "Alibaba", True, "China")
# proveedor3 = Proveedor("72.258.146-7", "Everlast S.A.", "Everlast", True, "USA")
# proveedor4 = Proveedor("15.063.978-5", "Tomás Leiva E.I.R.L.", "Tómas Shop", True, "Chile")
# proveedor5 = Proveedor("13.486.45", "Eduardo Carrasco S.A.", "Edo Store", True, "Chile")
# proveedor1.juridica_o_natural()