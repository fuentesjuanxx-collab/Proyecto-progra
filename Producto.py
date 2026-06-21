from Categoria import Categoria

class Producto_venta(Categoria):
    def __init__ (self, nombre,id_producto,valor,stock):
        super().__init__(nombre, id_producto)
        self.valor = valor
        self.stock=stock
        
    def __str__(self):
        return f"Producto:{self.nombre}\nStock en tienda:{self.stock}\nValor:{self.valor}Codigo del producto:{self.id_producto}"
class Producto_Tienda(Categoria):
    def __init__ (self, nombre,id_producto,uso):
        self.uso=uso
        super().__init__(nombre, id_producto)
    def __str__(self):
        return f"{self.nombre}{self.uso}{self.id_producto}"    
        
        