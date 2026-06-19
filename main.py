from Tienda import Tienda


T1=Tienda("Movil planeta")

print("Bienvenido a la familia Planeta movile \n ")
while True:
  while True:
    try:
        
        print("1)Crear Trabajador")
        print("2)Editar Trabajador")
        opc = int(input("Ingrese una opcion"))
        
        break  
    except ValueError:
        print(" Error: Por favor, ingrese un número entero válido.")
  #Creador de Trabajador 
  if opc==1:  
    E1=T1.crear_empleado()
  elif opc==2:
      T1.Editar()
  elif opc==3:
      T1.eliminar_()
  elif opc==4:
      for i in T1.empleados:
          print(i)
  elif opc==5:
      break
  else:
      print("El numero ingresado no esta en la lista de opciones.")







