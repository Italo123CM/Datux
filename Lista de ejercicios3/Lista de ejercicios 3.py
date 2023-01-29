#---------------------5---------------------------
import Modulo.Modulo as Mod
import os


def pordos(x):
    return x*2

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

class Producto:
    def __init__(self,Codigo):
        self.Codigo=Codigo
        self.Pais=Codigo.split("-")[0]
        self.NumLot=Codigo.split("-")[1]
        self.Año=Codigo.split("-")[2]
    def __str__(self):
        return "el pais de origen es: "+self.Pais+" y el numero de lote es: "+self.NumLot

               
#-------------------------------------------1----------------------------------------------
if(__name__=="__main__"):
#-------------------------------------2-------------------------------------------------
    texto="""Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.Lorem Ipsum ha sido el 
texto de relleno estándar de las industrias desde el año 1500, cuando unimpresor (N. del T. persona que se dedica a
la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos 
especimen."""

    print(texto.split(" "))
    print(" ".join(texto))
    print(texto.count("i"))
    print(texto.find("unimpresor"))
    print(texto.upper())
    print(texto.lower())
#-------------------------------3------------------------------------------

    print(pordos(2))

#--------------------------------4-----------------------------------------

    Autos=Catalogo()
    Auto1=producto("Ferrrari")
    Auto2=producto("toyota")
    Auto3=producto("Nisan")
    Auto4=producto("Audi")
    Auto5=producto("Lexus")
    Auto6=producto("Ford")
    Autos.agregar(Auto1.name)
    Autos.agregar(Auto2.name)
    Autos.agregar(Auto3.name)
    Autos.agregar(Auto4.name)
    Autos.agregar(Auto5.name)
    Autos.agregar(Auto6.name)
    Autos.mostrar()
#---------------------------5----8-----------------------
    try:
        print("escriba un numero entero ",end="")
        n=int(input("--> "))
        print("la suma de de los ",n,"primeros numeros es: ",Mod.SumaN(n))
        print("escriba un numero ",end="")
        n1=float(input("--> "))
        print("escriba un segundo numero ",end="")
        n2=float(input("--> "))
        print("la Divicion es: ",Mod.div(n1,n2))
    except ZeroDivisionError:
        print("ERROR: usted a dividido un numero por zero")
    else:
        print(os.getcwd())
    finally:
        print("proceso terminado")

#----------------------6---------------------------------
    print(__file__.split("\\")[-1])
    
#----------------------7----------------------
    Arroz=Producto("PERU-0118-2018")
    print(Arroz)

