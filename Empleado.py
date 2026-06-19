

class Empleado:
    def __init__(self,nombre,id_empleado,edad,correo):
        self.nombre=nombre
        self.id_empleado=id_empleado
        self.edad=edad
        self.correo=correo
        
    def __str__(self):
        return f"nombre:{self.nombre}-Id:{self.id_empleado}-Edad:{self.edad}-Correo:{self.correo}"
    
    
    
   
        