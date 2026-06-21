from Empleado import Empleado
from Tipo_de_pago import Boleta
from Producto import Producto_Tienda,Producto_venta
import random

class Tienda:
    def __init__(self,nombre):
        self.nombre=nombre
        self.productos_venta=[]
        self.productos_tienda=[]
        self.empleados=[]
        self.boletas=[]
        
    def __str__(self):
        return f"{self.nombre}{self.productos}{self.trabajadores}\n"
    def llenar_stock_ventas(self):
        self.productos_venta.append(Producto_venta("S229",2727,"Parlante", "Lenyes", 14990,4))
        self.productos_venta.append(Producto_venta("Tune 770 NC",1919,"Audifono", "JBL", 59990, 6))
        self.productos_venta.append(Producto_venta("G203",4646,"Mause", "logitec", 24990, 12))
        self.productos_venta.append(Producto_venta("Wave buds",3131,"audifonos","JBL", 44.990,8))
        self.productos_venta.append(Producto_venta("Watch 5 active",8282,"SmartWatch", "Xiaomi/Redmi", 34990, 10))
        return self.productos_venta
    def llenar_stock_tienda(self):
        self.productos_tienda.append(Producto_Tienda("Escoba", 1, 20))
        self.productos_tienda.append(Producto_Tienda("Trapero", 2, 20))
        self.productos_tienda.append(Producto_Tienda("Cloro", 3, 15))
        self.productos_tienda.append(Producto_Tienda("Limpia vidrios",4, 20))
        self.productos_tienda.append(Producto_Tienda("Pala", 5, 13))
        return self.productos_tienda
    def crear_boleta(self):
        total_boleta=0
        productos=[]
        encotrado=False
        while True:
            while True:
                for i in range(len(self.empleados)):
                    print("Ingrese su id para ingresar su venta")
                    id_Emp_b=verificador_de_enteros()
                    if id_Emp_b==self.empleados[i].id_empleado:
                        print(f"Se a ingresado con {self.empleados[i].nombre}")
                        vendedor=self.empleados[i].nombre
                        encotrado=True
                        break
                    else:
                        print("id invalido")
                if encotrado:
                    break
                    
            while True:
                print("1) Ingresar producto \n 2)Terminar boleta \n-",end="")
                opc_b=verificador_de_enteros()
                if opc_b==1:
                    for i in range(len(self.productos_venta)):
                        print("Ingrese el id del producto ")
                        id_prod_b=verificador_de_enteros()
                        
                        if id_prod_b==self.productos_venta[i].id_producto:
                            if self.productos_venta[i].stock<1:
                                print("Ya no queda stock de este producto, porfavor reponer")
                                
                                break
                            else:
                                total_boleta+=self.productos_venta[i].valor
                                self.productos_venta[i].stock-=1
                                productos.append(self.productos_venta[i].nombre)
                                print(f"La boleta lleva {total_boleta}")
                                
                                break

  
                elif opc_b==2:
                    return Boleta(vendedor, productos,total_boleta) 
                    break
                else:
                    print("La opcion ingresada no es valida")
     
               
    def mostrar_boleta(self):
        for i in range(len(self.boletas)):
            print(self.boletas[i])
    def mostrar_productos_B(self):
        for i in range(len(self.productos_venta)):
            print(self.productos_venta[i])
        
    
    def crear_empleado(self):
        
        contador_de_trabajador=1
        for _ in range(len(self.empleados)):
            contador_de_trabajador+=1
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
 






        
def verificador_de_enteros():       
    while True:
        try:
            opc = int(input("-"))
            break  
        except ValueError:
            print(" Error: Por favor, ingrese un número entero válido.")
    return opc   
          
          
          