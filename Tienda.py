from Empleado import Empleado
from Cliente import Tipo_de_pago
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
        print("Ingrese la edad del empleado \n",end="")
        edad=verificador_de_enteros()
        correo=input("Ingrese el correo del usuario\n-")
        
        Empleado(nombre, id_E, edad, correo)
        
        self.empleados.append(Empleado(nombre, id_E, edad, correo))
        print(f"Se a agregado Al empleado N°{contador_de_trabajador} \n")
        
        return self.empleados
    
    def editar_empleado(self):
        print("Ingrese el id Del usuario para verificar si existe en el sistema") 

        while True:
           for i in range(len(self.empleados)):
                
                id_Emp_edi=verificador_de_enteros()
                if id_Emp_edi==self.empleados[i].id_empleado:
                    print("1)Editar correo \n2)Editar edad")
                    opc=verificador_de_enteros()
                    print(opc)
                    break
                                   
           if opc==1:
                for i in range(len(self.empleados)):
                
                    if id_Emp_edi==self.empleados[i].id_empleado:
                    
                        correo=input(f"Ingrese el correo nuevo para:{self.empleados[i].nombre}\n")
                        self.empleados[i].correo=correo
                        print(f"Se a editado el correo de {self.empleados[i].nombre}")
                        break 
                break
           elif opc==2:
                for i in range(len(self.empleados)):
                
                   if id_Emp_edi==self.empleados[i].id_empleado:
                   
                       edad=input(f"Ingrese la edad nueva para:{self.empleados[i].nombre}\n")
                       self.empleados[i].edad=edad
                       print(f"Se a editado la edad de {self.empleados[i].nombre}")
                       break
                break    
           else:
                print("Opcion invalida")
                
               
    def eliminar_empleado(self):
        id_Emp_Elim=int(input("Ingrese el id del usuario para eliminar"))
        for i in range(len(self.empleados)):
            if id_Emp_Elim==self.empleados[i].id_empleado:
                print(f"Se a eliminado al empleado {self.empleados[i].nombre}\n")
                self.empleados.remove(self.empleados[i])
                break 
        
        return self.empleados
 
    def Crear_pago(self):
        tipo_pago=verificador_de_enteros()
        print("1)Efectivo \n2)Debito \n3)Credito")
        if tipo_pago ==1:            
            tipo_pago="Efectivo"
        elif tipo_pago ==1:            
            tipo_pago="Debito"
        elif tipo_pago ==1:            
            tipo_pago="Credito"
            
        self.cliente.append(Tipo_de_pago( tipo_pago))
        
        return self.Cliente
        
def verificador_de_enteros():       

    while True:
      try:
          opc = int(input("-"))
          
          break  
      except ValueError:
          print(" Error: Por favor, ingrese un número entero válido.")
    return opc    
          
          
          