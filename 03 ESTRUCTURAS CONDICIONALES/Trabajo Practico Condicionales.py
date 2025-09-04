#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

num_par = int(input("Ingrese un número: "))

if num_par % 2 == 0:
    print("El número ingresado es par.")
else:
    print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

categoria = int(input("Ingrese su edad: "))

if categoria < 12:
    print("Niño: Es menor de 12 años")
elif categoria >= 12 and categoria < 18:
    print("Adolescente: mayor o igual que 12 años y menor que 18 años.")
elif categoria >= 18 and categoria < 30:
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
elif categoria >= 30:
    print("#● Adulto/a: mayor o igual que 30 años.")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

password = input("Ingrese su contraseña: ")
if (len(password)) > 8 and (len(password)) < 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
#y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
#siguiente:

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1,100) for i in range(50)]

mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(f"Lista generada:")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
print(f"Moda: {moda}")

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo  o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

text = input("Ingrese una frase: ")
ultimo = text[-1]

if ultimo in "aeiouAEIOU":
    text = text + "!"
    print(text)
else:
    print(text)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:

name = input("Ingrese su nombre: ")
options = int(input("¿Cual opción desea usar para convertir su nombre? 1. Mayúsculas, 2. Minúsculas, 3. Solo la inicial con mayúscula "))

if options == 1:
    name = name.upper()
    print(name)
elif options == 2:
    name = name.lower()
    print(name)
elif options == 3:
    name = name.title()
    print(name)

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:

magnitud = int(input("¿De cuanto fue la magnitud del terremoto? "))

if magnitud < 3:
    print("Muy leve")
elif magnitud >=3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7:
    print("Extremo")

#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En cual hemisferio se encuentra? Sur/Norte ").lower
mes = input("Ingrese el mes en el que se encuentra: ").lower
dia = int(input("Ingrese en que día se encuentra: "))

