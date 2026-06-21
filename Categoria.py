class Categoria:
    def __init__(self,nombre,id_producto):
        self.nombre = nombre
        self.id_producto= id_producto    
    def __str__ (self):
        return f"{self.nombre} - {self.id_categoria} - {self.descripcion}"


