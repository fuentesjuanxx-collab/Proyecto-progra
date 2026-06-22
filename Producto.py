from Categoria import Categoria

class Producto_venta(Categoria):
    def __init__ (self, nombre,id_producto,tipo,marca,valor,stock):
        super().__init__(nombre, id_producto)
        self.tipo=tipo
        self.marca=marca
        self.valor = valor
        self.stock=stock
        
    def __str__(self):
        return f"Producto:{self.nombre}\nStock en tienda:{self.stock}\nMarca:{self.marca}\nValor:{self.valor}\nCodigo del producto:{self.id_producto}"
class Producto_Tienda(Categoria):
    def __init__ (self, nombre,id_producto,uso):
        self.uso=uso
        super().__init__(nombre, id_producto)
    def __str__(self):
        return f"{self.nombre}{self.uso}{self.id_producto}"    
        
        