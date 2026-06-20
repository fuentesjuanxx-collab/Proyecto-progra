class Empleado:
    def __init__(self,nombre,id_empleado,edad,correo):
        self.nombre=nombre
        self.id_empleado=id_empleado
        self.edad=edad
        self.correo=correo
        
    def __str__(self):
        return f"Nombre:{self.nombre}\nId:{self.id_empleado}\nEdad:{self.edad}\nCorreo:{self.correo}"
    
    
    
   
        