
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