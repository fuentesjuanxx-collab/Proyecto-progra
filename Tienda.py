from Empleado import Empleado
from Tipo_de_pago import Boleta
from Producto import Producto_Tienda, Producto_venta
import random

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos_venta = []
        self.productos_tienda = []
        self.empleados = []
        self.boletas = []
        
    def __str__(self):
        return f"{self.nombre}\n"

    def llenar_stock_ventas(self):
        self.productos_venta.append(Producto_venta("S229", 2727, "Parlante", "Lenyes", 14990, 4))
        self.productos_venta.append(Producto_venta("Tune 770 NC", 1919, "Audifono", "JBL", 59990, 6))
        self.productos_venta.append(Producto_venta("G203", 4646, "Mouse", "Logitech", 24990, 12))
        self.productos_venta.append(Producto_venta("Wave buds", 3131, "Audifonos", "JBL", 44990, 8))
        self.productos_venta.append(Producto_venta("Watch 5 active", 8282, "SmartWatch", "Xiaomi/Redmi", 34990, 10))
        return self.productos_venta

    def llenar_stock_tienda(self):
        self.productos_tienda.append(Producto_Tienda("Escoba", 1, 20))
        self.productos_tienda.append(Producto_Tienda("Trapero", 2, 20))
        self.productos_tienda.append(Producto_Tienda("Cloro", 3, 15))
        self.productos_tienda.append(Producto_Tienda("Limpia vidrios", 4, 20))
        self.productos_tienda.append(Producto_Tienda("Pala", 5, 13))
        return self.productos_tienda

    def crear_boleta(self):
        encotrado = False
        
        while True:
            while True:
                print("Ingrese su ID para ingresar su venta:")
                id_Emp_b = verificador_de_enteros()
                
                for i in range(len(self.empleados)):
                    if id_Emp_b == self.empleados[i].id_empleado:
                        print(f"Se ha ingresado con el empleado: {self.empleados[i].nombre}\n")
                        vendedor_objeto = self.empleados[i]
                        encotrado = True
                        break
                
                if encotrado:
                    break
                else:
                    print("ID inválido.\n")
                    
            nueva_boleta = Boleta(vendedor_objeto)
            
            while True:
                print("1) Ingresar producto\n2) Terminar boleta\n-")
                opc_b = verificador_de_enteros()
                print("\n")
                
                if opc_b == 1:
                    print("Ingrese el ID del producto:")
                    id_prod_b = verificador_de_enteros()
                    producto_encontrado = False
                    
                    for i in range(len(self.productos_venta)):
                        if id_prod_b == self.productos_venta[i].id_producto:
                            producto_encontrado = True
                            
                            if self.productos_venta[i].stock < 1:
                                print("Ya no queda stock de este producto, por favor reponer.\n")
                            else:
                                nueva_boleta.producto.append(self.productos_venta[i].nombre)
                                nueva_boleta.total += self.productos_venta[i].valor
                                self.productos_venta[i].stock -= 1
                                print(f"Monto acumulado en boleta: ${nueva_boleta.total}\n")
                            break
                    
                    if not producto_encontrado:
                        print("El ID ingresado no está en el sistema.\n")
      
                elif opc_b == 2:
                    vendedor_objeto.total_ventas += nueva_boleta.total
                    self.boletas.append(nueva_boleta)
                    return nueva_boleta
                else:
                    print("La opción ingresada no es válida.\n")
               
    def mostrar_boleta(self):
        for i in range(len(self.boletas)):
            print(self.boletas[i])

    def mostrar_productos_B(self):
        for i in range(len(self.productos_venta)):
            print(self.productos_venta[i])
        
    def crear_empleado(self):
        contador_de_trabajador = 1
        for _ in range(len(self.empleados)):
            contador_de_trabajador += 1
            
        nombre = input("Ingrese el nombre del empleado:\n- ")
                        
        id_E = random.randint(1000, 9999)
        print("Ingrese la edad del empleado:")
        edad = verificador_de_enteros()
        correo = input("Ingrese el correo del usuario:\n- ")
        
        self.empleados.append(Empleado(nombre, id_E, edad, correo))
        print(f"Se ha agregado al empleado N° {contador_de_trabajador} con éxito.\n")
        return self.empleados
    
    def editar_empleado(self):
        print("Ingrese el ID del usuario para verificar si existe en el sistema:") 
        while True:
            id_Emp_edi = verificador_de_enteros()
            empleado_encontrado = False
            
            for i in range(len(self.empleados)):
                if id_Emp_edi == self.empleados[i].id_empleado:
                    print("1) Editar correo\n2) Editar edad\n-")
                    opc = verificador_de_enteros()
                    empleado_encontrado = True
                    break
            
            if not empleado_encontrado:
                print("ID no encontrado. Intente nuevamente:")
                continue
                                    
            if opc == 1:
                for i in range(len(self.empleados)):
                    if id_Emp_edi == self.empleados[i].id_empleado:
                        correo = input(f"Ingrese el correo nuevo para {self.empleados[i].nombre}:\n- ")
                        self.empleados[i].correo = correo
                        print(f"Se ha editado el correo de {self.empleados[i].nombre}.\n")
                        break 
                break
            elif opc == 2:
                for i in range(len(self.empleados)):
                    if id_Emp_edi == self.empleados[i].id_empleado:
                        print(f"Ingrese la edad nueva para {self.empleados[i].nombre}:")
                        edad = verificador_de_enteros()
                        self.empleados[i].edad = edad
                        print(f"Se ha editado la edad de {self.empleados[i].nombre}.\n")
                        break
                break    
            else:
                print("Opción inválida.\n")
                            
    def eliminar_empleado(self):
        print("Ingrese el ID del usuario para eliminar:")
        id_Emp_Elim = verificador_de_enteros()
        
        for i in range(len(self.empleados)):
            if id_Emp_Elim == self.empleados[i].id_empleado:
                print(f"Se ha eliminado al empleado {self.empleados[i].nombre}.\n")
                self.empleados.remove(self.empleados[i])
                break 
        return self.empleados

def verificador_de_enteros():       
    while True:
        try:
            opc = int(input("- "))
            break  
        except ValueError:
            print("\nError: Por favor, ingrese un número entero válido.\n")
    return opc