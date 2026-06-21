class Producto:
    def __init__ (self, nombre, stock, valor, id_producto):
        self.nombre = nombre
        self.stock = stock
        self.valor = valor
        self.id_producto = id_producto

    def __str__(self):
        return f"{self.nombre}{self.stock}{self.valor}{self.id_producto}"
    
    def agregar_producto(self):
        nombre = str(input("Ingrese el nombre del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        valor = int(input("Ingrese el valor del producto: "))
        id_producto = int(input("Ingrese el ID del producto: "))