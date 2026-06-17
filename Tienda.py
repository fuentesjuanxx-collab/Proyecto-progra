class Tienda:
    def __init__(self,nombre):
        self.nombre=nombre
        self.productos=[]
        self.trabajadores=[]
        
    def __str__(self):
        return f"{self.nombre}{self.productos}{self.trabajadores}"
    
    
    