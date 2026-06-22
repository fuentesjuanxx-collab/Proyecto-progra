class Boleta:
    def __init__(self,vendedor):
        self.producto=[]
        self.vendedor=vendedor
        self.total=0

    def __str__(self):
        return f"Vendedor:{self.vendedor} \nProductos:{self.producto} \nTotal de la boleta{self.total} \n "











