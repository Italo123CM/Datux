#Soy el alumno Rodrigo Italo Cayo Mamani
#Realizar un programa que ingrese sus datos personales e imprimirlos.
print("PREGUNTA Nº1")

nom = input("Ingresa tus nombres :")
apell = input("Ingresa tus apellidos: ")
edad = input("Ingresa tu edad: ")
dni  = input("Ingrese el numero de su dni: ")
print("Mi nombre es "+ nom + ", mis apellidos son "+ apell+ " y mi edad es: " + edad +", identificado con el numero de dni " +dni)
print("--------------------------")

#Calcule el área de un círculo, triángulo equilatero y cuadrado con radio ingresado desde el teclado
print("Pregunta N2")
print("3.Ingrese 3 valores y realice las operaciones de suma ,resta ,multiplicación, división y división entera.")
import math
radio = float(input(' Ingrese tamaño del radio : '))
AreaCirculo = float((radio ** 2) *math.pi)
print("El area del circulo es : ",AreaCirculo)
lado = float(input('\nIngrese el lado para calcular el area del cuadrado: '))
AreaCuadrado = (( lado**2 ))
print("El area del cuadrado es : ",AreaCuadrado)
base= float(input('\nIngrese la base para calcular el area del triangulo: '))
altura = float(input('Ingrese la altura para calcular el area del triangulo: '))
AreaTriangulo = (base*altura/2)
print("El area del triangulo es : ",AreaTriangulo)
print("--------------------------")

print("Pregunta N3")
print("3.Ingrese 3 valores y realice las operaciones de suma ,resta ,multiplicación, división y división entera.")
numero=float(input("Ingresa el valor del primer numero: "))
numero2=float(input("Ingresa el valor del segundo numero: "))
numero3=float(input("Ingresa el valor del tercer numero: "))
print("La suma de los tres numeros es: ", numero+numero2+numero3)
print("La resta de los tres numeros es: ", numero-numero2-numero3)
print("La multiplicacion de los tres numeros es: ", numero*numero2*numero3)
print("La division de los tres numeros es: ", numero/numero2/numero3)
print("La division entera de los tres numeros es: ", numero//numero2//numero3)
print("--------------------------")

print("Pregunta N4")
print("#Ingrese un valor e imprima el tipo de dato.")
dato= input("Ingrese el dato: ")
print(type(dato))
print("--------------------------")

print("Pregunta N5")
print("Realice un programa que imprima la ubicación de su carpeta donde se encuentra trabajando")
import sys
ubicacion = sys.argv[0]
print("La ubicacion es \n\t ",ubicacion)
print("--------------------------")

print("Pregunta N6")
print("Realice un programa que calcule la suma de los números hasta el valor ingresado.Ejemplo : si se ingresa 5 se tendrá que calcular 1+2+3+4+5.")
cantidad= int(input("Ingrese la cantidad de terminos a sumar:"))
suma=0
for i in range (1,cantidad+1):
  suma +=i
print("La suma total de los terminos es :" ,suma)
print("--------------------------")

print("Ejercicio N7")
print("""7. Realiza un programa que lea 2 números por teclado y determine los siguientes
aspectos:
● Si los dos números son iguales
● Si los dos números son diferentes
● Si el primero es mayor que el segundo
● Si el segundo es mayor o igual que el primero""")

x = float(input("Ingrese el primer valor:"))
y = float(input("Ingrese el segundo valor:"))

print("Los numeros son iguales ",x==y)
print("Los numeros son diferentes", x!=y)
print("El primero numero es mayor que el segundo",x>y)
print("El segundo numero es mayor o igual que el primero",y>=x)
print("--------------------------")

print("Ejercicio N8")
print("Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.")

contraseña ="contraseña"
palabra=input("Ingrese la contraseña:")
if(contraseña==palabra.lower()):
  print("La contraseña es la misma")
else:
  print("La contraseña no es la correcta")
  print("--------------------------")
