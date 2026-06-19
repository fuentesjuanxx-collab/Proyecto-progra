from Empleado import Empleado


class Tienda:
    def __init__(self,nombre):
        self.nombre=nombre
        self.productos=[]
        self.trabajadores=[]
        
    def __str__(self):
        return f"{self.nombre}{self.productos}{self.trabajadores}"
    
    def crear_empleado(self):
        contador_de_empleados=0
        nombre=input("Ingrese el nombre del Empleado")
        for i in self.trabajadores:
            contador_de_empleados+=1
        id_E=contador_de_empleados
        edad=int(input("Ingrese la edad del empleado"))
        correo=input("Ingrese el correo del usuario")
        Empleado(nombre, id_E, edad, correo)
        self.trabajadores.append(Empleado(nombre, id_E, edad, correo))
        print("Se a agregado Al trabajador N{contador_de_empleados}")
        
        return self.trabajadores
    
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    