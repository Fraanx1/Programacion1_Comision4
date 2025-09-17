#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0,101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = int(input("Ingrese un número: "))
digitos = len(str(num))

print(f"El número {num} tiene {digitos} digitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

menor = min(num1, num2)
mayor = max(num1, num2)

suma = 0
for i in range(menor + 1, mayor):
    suma += i
print(f"La suma de los números entre {num1} y {num2} es de {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

num = 1
suma_v = 0
while num != 0:
    num = int(input("Ingrese un número: "))
    suma_v = suma_v + num
    num = int(input("¿Desea seguir sumando números? Si: 1 / No: 0: "))

print(suma_v)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num_aleatorio = random.randint(0,9)
intentos = 0
adivinar = -1

print("Adivina el número aleatorio")

while adivinar != num_aleatorio:
    adivinar = int(input("Ingrese un número: "))
    intentos = intentos + 1

print(f"El numero correcto era {num_aleatorio}, lo adivinaste en {intentos} intentos")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range(100,1,-2):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

suma = 0
n = int(input("Ingrese un número: "))

for i in range(0, n + 1):
    suma = suma + i
print(f"La suma de los números comprendidos de 0 hasta {n} es de {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

par = 0
impar = 0
neg = 0
posi = 0
for i in range(1,101):
    num3 = int(input("Ingrese números: "))
    if num3 % 2 == 0:
        par = par + 1
    elif num3 % 2 != 0:
        impar = impar + 1

    if num3 < 0:  
        neg = neg + 1
    elif num3 > 0:
        posi = posi + 1
print(f"Ha ingresado {par} números pares")
print(f"Ha ingresado {impar} números impares")
print(f"Ha ingresado {neg} números negativos")
print(f"Ha ingresado {posi} números positivos")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).

suma = 0

for i in range(1,101):
    suma_num = int(input("Ingrese números: "))
    suma = suma + suma_num
media = suma / 101
print(f"La media de los números ingresados es de {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num4 = int(input("Ingrese un número: "))

invertido = 0

while num4 > 0:
    digito = num4 % 10
    invertido = invertido * 10 + digito
    numero = num4 // 10

print(f"El número invertido es: {invertido}")