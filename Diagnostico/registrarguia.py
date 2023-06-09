import guia

class Contribuyente:
    
    def __init__(self, nombre, apellido, cuit):
        self.nombre = nombre
        self.apellido = apellido
        self.cuit = cuit

class ValidadorAFIP:
   
    contribuyentes = [Contribuyente("Juan", "Perez", 2044873351), Contribuyente("Maria", "Gomez", 2044873362)]
   
    def buscarcuit(self, cuit):
        for contribuyente in ValidadorAFIP.contribuyentes:
            if contribuyente.cuit == cuit:
                return contribuyente 
        return None

class Controller:
    def validardatos(self, nombre, apellido, cuit):
        
        validador = ValidadorAFIP()
        contribuyente = validador.buscarcuit(cuit)

        if contribuyente is None:
            print("El CUIT no existe")
            return 
        if contribuyente.nombre != nombre or contribuyente.apellido != apellido:
            print("Los datos no coinciden")
            return 
        
        print("Los datos son correctos")
        
        guiaA = guia.Guia(nombre, apellido, cuit)
        return guiaA

class IU:
    @staticmethod
    def registrarguia():
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        cuit = int(input("Ingrese su CUIT: "))

        controller = Controller()


        guia = controller.validardatos(nombre, apellido, cuit)
        
        if guia == None:
            print("El guia no pudo ser registrado")
            return

        contrasena = input("Ingrese su contrasena: ")

        guia.contrasena = contrasena

        print("Su usuario fue creado con exito")

        persistencia = Persistencia()
        persistencia.guardarguia(guia)

class Persistencia():
    guias = []

    def guardarguia(self, guia):
        Persistencia.guias.append(guia)

IU.registrarguia()
