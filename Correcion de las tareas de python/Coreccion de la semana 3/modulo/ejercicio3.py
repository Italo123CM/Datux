
class Catalogo:
    def __init__(self):
        self.productos=[]
    def agregar(self,producto):
        self.productos.append(producto)
    def mostrar(self):
        print(self.productos)

class producto:
    def __init__(self,name):
        self.name=name