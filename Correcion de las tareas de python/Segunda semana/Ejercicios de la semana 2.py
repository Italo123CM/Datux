##Ejercicios de la semana2
print("Ejercicio N1")
print("Realizar un Menú Iterativo que tenga las siguientes opciones(Solo poner el número de la pregunta:")
##defino primero las listas
listadenumeros= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,20,22,23,24,25,26,27,28,29,30]
edadesdepersonas= [['Italo', 19], ['Julio', 16], ['Flor', 31], ['Rosa', 21]]

while True:
    print("Selecciona la opcion que requiera: ")
    print("1. Dibujar un cuadrado en consola con *")
    print("2. Identificar si un número es múltiplo de 2")
    print("3. Imprimir solo los mayores de edad")
    print("4. Salir")
    opcion = int(input())
    if opcion == 1:
        tamaño = int(input("Ingresa el tamaño que desees que tenga el cuadrado: "))
        print("\n")
        for i in range(tamaño):
            for j in range(tamaño):
                print("*", end=" ")
            print()
    elif opcion == 2:
        print("Analizando la lista : ",listadenumeros)
        for numero in listadenumeros:
            if numero % 2 == 0:
                print("El numero ",numero, " es multiplo de dos")
    elif opcion == 3:
        print("Analizando la lista : ",edadesdepersonas)
        print("Mostrando personas mayores de edad :")
        for persona in edadesdepersonas:
            if persona[1] >= 18:
                print(persona[0]," tiene ",persona[1])
    elif opcion == 4:
        break
    print("\n")
    print("Programa finalizado")
    print("----------------------------------------")

    print("Ejercicio N2")
print("""Realizar un Programa que simule funcionalidades de una Biblioteca, definir la biblioteca
como un diccionario.
2.1 La biblioteca deberá tener las siguientes operaciones:
- Obtener la lista de categorías de libros.
-Obtener nombres de los libros y autores.
-poder cambiar el estado de un libro a prestado
-Lista de usuarios de la biblioteca.""")
biblioteca={
    "nombreBiblioteca":"Biblioteca Nacional del Perú",
    "genero":["terror","literatura","comedia","tragedia"],
    "nombreLibro":{
        "ALTAR":{"autor":"Catherine Lacey",
                "genero": ["terror"],
                "codLibro":"1",
                "estado":"Libre"
                },
        "DON QUIJOTE DE LA MANCHA":{"autor":"Miguel de Cervantes Saavedra",
                "genero":["literatura"],
                "codLibro":"2",
                "estado":"Libre"
                },
        "MALDITO KARMA":{"autor":"David Safier",
                "genero":["comedia"],
                "codLibro":"3",
                "estado":"Prestado"
                },
         "ENTRE DOS LUNAS":{"autor":"Sharon Creech",
                "genero":["tragedia"],
                "codLibro":"4",
                "estado":"Prestado"
                }
    },
    "usuario":{
        "ITALO":{
            "nombreLibro":["Entre dos lunas"]
            },
        "ROSA":{
            "nombreLibro":["Maldito karma"]
            },
        
        }
    }


msg = """
Menú
1) Lista de categorias de libro
2) Nombre de los libros y autores 
3) Cambiar estado de libro a prestado
4) Lista de usuarios de la biblioteca
5) Salir
"""
while True:
    print(msg)
    op=input("Elija una de las siguientes opciones: ")
    if op =='1':
        print(biblioteca['genero'])
    elif op=='2':
        nombreLibros=list(biblioteca["nombreLibro"].items())
         ##print(nombreLibros)
        for x in biblioteca['nombreLibro'].keys():
            print("-Apartado-")
            print("nombre: ", x)
            autorLibro=biblioteca['nombreLibro'][x]["autor"]
            print("autor:  ", autorLibro)
    elif op=='3':
        nomLibro=input("Ingrese el nombre del libro: ").upper()
        listaLibros=list(biblioteca['nombreLibro'].keys())
        ##print(listaLibros)
        if nomLibro in listaLibros:
            ##print("Libro existe")
            estadoLibro=biblioteca['nombreLibro'][nomLibro]['estado']
            if(estadoLibro=='Libre'):
                print("El libro está disponible")
                nombre=input("Ingrese el nombre del usuario al que se le va a prestar el libro: ").upper()
                usuarios=list(biblioteca["usuario"].keys())
                if(nombre in usuarios):
                    agregarLibro=biblioteca["usuario"][nombre]["nombreLibro"]
                    agregarLibro.append(nomLibro)
                    biblioteca['nombreLibro'][nomLibro]['estado']={'estado':'Prestado'}
                    print(biblioteca['nombreLibro'][nomLibro]['estado'])
                    print("Cambio de estado realizado correctamente")
                    print(biblioteca)
                else:
                    print("El usuario no se encuentra en el sistema")
            else:
                print("El libro ya se encuentra prestado")
        else:
            print("El libro no esta en el repositorio de la biblioteca") 
    elif op=='4':
        usuarios=biblioteca["usuario"].keys()
        print(usuarios)
    elif op=='5':
        print("Muchas gracias!")
        break
    else:
        print("Ingrese una opción válida")
        print("----------------------------------------")

print("Ejercicio N3")
print("Definir una funcion que retorne el mayor valor al ingresar dos numeros")

x=int(input("ingresa tu primer numero: "))
y=int(input("ingrese el segundo numero: "))
def mayor(x,y):
  if(x!=y):
    if x>y:
        print(str(x)+ ' es mayor que '+str(y))
    else:
      print(str(y)+ ' es mayor que '+str(x))
mayor(x,y)
print("----------------------------------------")

print("Ejercicio N4:")
print("Definir una función que imprima los argumentos ingresados desde línea de comandos Nota: Usar import sys.argv => *args")
import sys
op=int(input("Ingresa la cantidad de argumentos: "))
lista=[]
def ingreso(op):
    for x in range(0,op):
        lista.append(input(f"El argumento numero {x+1} es: "))
    return lista

def imprimirArgumentos(*args):
    for arg in args:
        print(arg)
        
imprimirArgumentos(ingreso(op))
print("----------------------------------------")