from Tienda import Tienda

def verificador_de_enteros():       
    while True:
        try:
            opc = int(input("-"))
            break  
        except ValueError:
            print(" Error: Por favor, ingrese un número entero válido.")
    return opc   

T1 = Tienda("Movil planeta")

print("=========================================")
print(" Bienvenido a la familia Planeta Móvil ")
print("=========================================\n")

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1) Abrir Tienda (Cargar Stock Inicial)")
    print("2) Gestión de Trabajadores ")
    print("3) Crear Boleta (Realizar Venta) ")
    print("4) Mostrar Historial de Boletas ")
    print("5) Mostrar Productos en Venta ")
    print("6) Salir del Sistema") 
    print("------------------------")
    print("Ingrese una opción:")
    
    opc = verificador_de_enteros()
    print("") 
    
    if opc == 1:  
        T1.llenar_stock_tienda()
        T1.llenar_stock_ventas()
        print("Ha abierto Movil Planeta y se ha cargado el stock")

    elif opc == 2:
        while True:
            print("       TRABAJADORES ")
            print("1) Registrar Nuevo Trabajador")
            print("2) Editar Datos de Trabajador")
            print("3) Eliminar Trabajador de Sistema")
            print("4) Listar Todos los Trabajadores")
            print("5) Volver al Menú Principal \n")
            
            print("Ingrese una opción de trabajador:")
            
            opc_trabajador = verificador_de_enteros()
            print("")
            
            if opc_trabajador == 1:
                T1.crear_empleado()
            elif opc_trabajador == 2:
                T1.editar_empleado()
            elif opc_trabajador == 3:
                T1.eliminar_empleado()
            elif opc_trabajador == 4:
                if T1.empleados == []:
                    print("No hay trabajadores registrados todavía.")
                else:
                    print("Lista de trabajadores ")
                    for empleado in T1.empleados:
                        print(f"{empleado} ")
            elif opc_trabajador == 5:
                print("Volviendo al menú principal...")
                break 
            else:
                print("Opción inválida dentro del submenú.")
                
    elif opc == 3:
        if T1.empleados == []:
            print("No se puede vender si no hay empleados creados en el sistema.")
        elif T1.productos_venta == []:
            print("La tienda está cerrada. Primero selecciona la opción 1 para cargar los productos.")
        else:
            T1.crear_boleta()
            
    elif opc == 4:
        if T1.boletas == []:
            print("No se han realizado ventas ni generado boletas hoy.")
        else:
            print("Boletas emitidas")
            T1.mostrar_boleta()
            
    elif opc == 5:
        if T1.productos_venta == []:
            print("No hay stock cargado. Recuerda usar la opción 1.")
        else:
            print("Productos para la venta")
            T1.mostrar_productos_B()
            
    elif opc == 6:
        print("Saliendo del sistema de Movil Planeta...")
        break         
        
    else:
        print("El número ingresado no está en la lista de opciones.")







