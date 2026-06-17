class Categoria:
    def __init__(self,nombre,id_categoria,descripcion):
        self.nombre = nombre
        self.id_categoria = id_categoria
        self.descripcion = descripcion
    
    def __str__ (self):
        return f"{self.nombre}{self.id_categoria}{self.descripcion}"
    
    
