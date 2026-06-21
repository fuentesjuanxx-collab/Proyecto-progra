from Producto import Producto
class Categoria:
    def __init__(self,nombre,id_categoria,descripcion):
        self.nombre = nombre
        self.id_categoria = id_categoria
        self.descripcion = descripcion
        self.producto = []
    
    def __str__ (self):
        return f"{self.nombre} - {self.id_categoria} - {self.descripcion}"
    
    def agregar_producto(self,producto):
        self.producto.append(producto)

    def mostrar_producto(self):
        for producto in self.producto:
            print(producto)

Categoria1 = Categoria("Audifonos", 5, "Accesorio de audio")
producto1  = Producto("AirPods", 8, 12000, 77996658)
producto2 = Producto("JBL", 5, 2500, 7788445)
Categoria1.agregar_producto(producto1)
Categoria1.agregar_producto(producto2)
Categoria1.mostrar_producto()