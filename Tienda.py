from Empleado import Empleado
from Cliente import Cliente

class Tienda:
    def __init__(self,nombre):
        self.nombre=nombre
        self.productos=[]
        self.trabajadores=[]
        self.cliente=[]
        
    def __str__(self):
        return f"{self.nombre}{self.productos}{self.trabajadores}"
    
    def crear_trabajador(self):
        contador_de_empleados=0
        nombre=input("Ingrese el nombre del trabajador\n-")
        
        for i in self.trabajadores:
            contador_de_empleados+=1
            
        id_E=contador_de_empleados
        edad=int(input("Ingrese la edad del empleado \n-"))
        correo=input("Ingrese el correo del usuario\n-")
        Empleado(nombre, id_E, edad, correo)
        self.trabajadores.append(Empleado(nombre, id_E, edad, correo))
        print("Se a agregado Al trabajador N{contador_de_empleados}")
        
        return self.trabajadores
    def crear_cliente(self):
        
        nombre=input("Nombre del Cliente \n-")
        tipo_pago=int(input("Ingrese el tipo de pago \n-1)Efectivo \n-2)Debito"))
        
        if tipo_pago ==1:            
            tipo_pago="Efectivo"
        else:
            
            tipo_pago="Debito"
        self.cliente.append(Cliente(nombre, tipo_pago))
        
        return self.Cliente
        
        
        
        
        
        
        
        
        
        
        
        
    