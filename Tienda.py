from Empleado import Empleado
from Cliente import Cliente
import random
class Tienda:
    def __init__(self,nombre):
        self.nombre=nombre
        self.productos=[]
        self.empleados=[]
        self.cliente=[]
        
    def __str__(self):
        return f"{self.nombre}{self.productos}{self.trabajadores}\n"
    
    def crear_empleado(self):
        contador_de_trabajador=1
        nombre=input("Ingrese el nombre del empleado\n-")
                        
        id_E=random.randint(1000,9999)
        
        edad=int(input("Ingrese la edad del empleado \n-"))
        correo=input("Ingrese el correo del usuario\n-")
        
        Empleado(nombre, id_E, edad, correo)
        
        self.empleados.append(Empleado(nombre, id_E, edad, correo))
        print(f"Se a agregado Al empleado N°{contador_de_trabajador} \n")
        
        return self.empleados
    
    def editar_empleado(self):
        
       while True: 
            while True:
              try:
                  id_Emp_edi=int(input("Ingrese el id del usuario para editar empleado\n-"))
                  print("1)Nombre \n 2)Correo \n3)Edad")
                  break  
              except ValueError:
                  
                  print(" Error: Por favor, ingrese un número entero válido.")
    
            if id_Emp_edi==1:
                for i in range(len(self.empleados)):
                    
                    if id_Emp_edi==self.empleados[i].id_empleado:
                        
                        print(f"Se a eliminado al empleado {self.empleados[i].nombre}\n")
                        self.empleados.replace(self.empleados[i])
                        break 
                break
            elif id_Emp_edi==2:
                for i in range(len(self.empleados)):
                    
                    if id_Emp_edi==self.empleados[i].id_empleado:
                        
                        print(f"Se a eliminado al empleado {self.empleados[i].nombre}\n")
                        self.empleados.replace(self.empleados[i])
                        break   
                break
            
        
        
    
    
    def eliminar_empleado(self):
        id_Emp_Elim=int(input("Ingrese el id del usuario para eliminar"))
        for i in range(len(self.empleados)):
            if id_Emp_Elim==self.empleados[i].id_empleado:
                print(f"Se a eliminado al empleado {self.empleados[i].nombre}\n")
                self.empleados.remove(self.empleados[i])
                break 
        
        return self.empleados
 
    def Crear_pago(self):
        while True:
          try:
              tipo_pago=int(input("Ingrese el tipo de pago \n-1)Efectivo \n-2)Debito \n-3)Credito"))
              
              break  
          except ValueError:
              print(" Error: Por favor, ingrese un número entero válido.")
        
        
        if tipo_pago ==1:            
            tipo_pago="Efectivo"
        elif tipo_pago ==1:            
            tipo_pago="Debito"
        elif tipo_pago ==1:            
            tipo_pago="Credito"
            
        self.cliente.append(Cliente( tipo_pago))
        
        return self.Cliente
        
        
        
        
        
        
        
        
        
        
        
def verificador_de_enteros(opc):       

    while True:
      try:
          opc = int(input("Ingrese el un valor numerico"))
          
          break  
      except ValueError:
          print(" Error: Por favor, ingrese un número entero válido.")
          
          
          
          