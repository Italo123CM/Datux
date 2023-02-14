#---------------------5---------------------------
from modulo.ejercicio1 import *
from modulo.ejercicio2 import *
from modulo.ejercicio3 import *
from modulo.ejercicio4 import *
from modulo.ejercicio5 import *

import os
            
#-------------------------------------------1----------------------------------------------
if(__name__=="__main__"):
#-------------------------------------2-------------------------------------------------
    print("EJERCICIO 2")
    texto="""Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.Lorem Ipsum ha sido el 
texto de relleno estándar de las industrias desde el año 1500, cuando unimpresor (N. del T. persona que se dedica a
la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos 
especimen."""

    while True:
        print("""
                Menú de Funciones de String    
        -----------------------------------------
        1 = Texto a Split
        2 = Texto a Join
        3 = Texto a Count
        4 = Texto a Find
        5 = Texto a Upper
        6 = Texto a Lower
        7 = Salir""")

        print("\n") 
        opcion = int(input("Selecciona una de las opciones dadas: "))
        print("\n") 

        if opcion == 1:
            print("TEXTO MODIFICADO A SPLIT: ")
            texto_split(texto)
            print("-----------------------------------------")

        elif opcion == 2:
            print("TEXTO MODIFICADO A JOIN: ")
            texto_join(texto)
            print("-----------------------------------------")

        elif opcion == 3:
            print("TEXTO MODIFICADO A COUNT: ")
            texto_count(texto)
            print("-----------------------------------------")

        elif opcion == 4:
            print("TEXTO MODIFICADO A FIND: ")
            texto_find(texto)
            print("-----------------------------------------")

        elif opcion == 5:
            print("TEXTO MODIFICADO A UPPERCASE: ")
            texto_upper(texto)
            print("-----------------------------------------")

        elif opcion == 6:
            print("TEXTO MODIFICADO A LOWERCASE: ")
            texto_lower(texto)
            print("-----------------------------------------")

        elif opcion == 7:
            print("Gracias, saliendo del programa")
            print("-----------------------------------------")
            print("\n") 
            break
            
        else:
            print("Opcion no encontrada, vuelva a digitar una opcion")

#-------------------------------3------------------------------------------
    print("EJERCICIO 3")
    num=int(input("Ingrese un numero a calcular: "))
    print("El resultado es: ",por_dos(num))
    print("\n") 

#--------------------------------4-----------------------------------------
    #Agregamos productos al catalogo:
    print("EJERCICIO 4")
    Autos=Catalogo()
    Auto1=producto("Ferrrari")
    Autos.agregar(Auto1.name)

    Auto2=producto("toyota")
    Autos.agregar(Auto2.name)

    Auto3=producto("Nisan")
    Autos.agregar(Auto3.name)
 
    Auto4=producto("Audi")
    Autos.agregar(Auto4.name)

    Auto5=producto("Lexus")
    Autos.agregar(Auto5.name)

    Auto6=producto("Ford")
    Autos.agregar(Auto6.name)

    print("LA LISTA COMPLETA DEL CATALOGO DE AUTOS: ")
    Autos.mostrar()
    print("\n") 

#---------------------------5 y 8-----------------------
    print("EJERCICIO 5 Y 8")
    try:
        print("Escriba un numero entero ",end="")
        n=int(input("--> "))
        print("La suma de de los ",n,"primeros numeros es: ",SumaN(n))
        print("\n") 

        print("Escriba un numero ",end="")
        n1=float(input("--> "))
        print("Escriba un segundo numero ",end="")
        n2=float(input("--> "))
        print("La Division es: ",div(n1,n2))
    except ZeroDivisionError:
        print("ERROR: usted a dividido un numero por zero")
    else:
        print(os.getcwd())
    finally:
        print("proceso terminado")
    print("\n") 

#----------------------6---------------------------------
    print("EJERCICIO 6")
    print("El archivo en ejecucion es: ")
    print(__file__.split("\\")[-1])
    print("\n") 
    
#----------------------7----------------------
    print("EJERCICIO 7")
    Arroz=Producto("PERU-0118-2018")
    print(Arroz)
    print("\n") 