class Producto:
    def __init__(self,Codigo):
        self.Codigo=Codigo
        self.Pais=Codigo.split("-")[0]
        self.NumLot=Codigo.split("-")[1]
        self.Año=Codigo.split("-")[2]
    def __str__(self):
        return "el pais de origen es: "+self.Pais+" y el numero de lote es: "+self.NumLot