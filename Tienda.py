from Empleado import Empleado
from Cliente import Cliente

class Tienda:
    def __init__(self,nombre):
        self.nombre=nombre
        self.productos=[]
        self.empleados=[]
        self.cliente=[]
        
    def __str__(self):
        return f"{self.nombre}{self.productos}{self.trabajadores}"
    
    def crear_empleado(self):
        contador_de_trabajador=1
        nombre=input("Ingrese el nombre del empleado\n-")
                        
        id_E=len(self.empleados)+1
        
        edad=int(input("Ingrese la edad del empleado \n-"))
        correo=input("Ingrese el correo del usuario\n-")
        
        Empleado(nombre, id_E, edad, correo)
        
        self.empleados.append(Empleado(nombre, id_E, edad, correo))
        print(f"Se a agregado Al empleado N°{contador_de_trabajador}")
        
        return self.empleados
    
    def editar_empleado(self):
        pass
        
    
    
    def eliminar_(self):
        id_Emp_Elim=int(input("Ingrese el id del usuario para eliminar"))
        for i in range(len(self.empleados)):
            if id_Emp_Elim==self.empleados[i].id_empleado:
                print(f"Se a eliminado al empleado {self.empleados[i].nombre}")
                self.empleados.remove(self.empleados[i])
                break 
        
        return self.empleados
 
    def crear_cliente(self):
        
        nombre=input("Nombre del Cliente \n-")
        tipo_pago=int(input("Ingrese el tipo de pago \n-1)Efectivo \n-2)Debito"))
        
        if tipo_pago ==1:            
            tipo_pago="Efectivo"
        else:
            
            tipo_pago="Debito"
        self.cliente.append(Cliente(nombre, tipo_pago))
        
        return self.Cliente
        
        
        
        
        
        
        
        
        
        
        
        
    