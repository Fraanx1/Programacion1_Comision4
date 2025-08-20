#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado

nombre = input ("Ingrese su nombre: ")
print(f"Hola {nombre}")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados.

nombre = input ("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
print (f"Soy {nombre +" "+ apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

radio = float(input("Ingrese el radio del circulo: "))
area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio
print(f"El area del circulo es {area}, y el perimetro es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos = int(input("Ingrese la cantidad de segundos que desea: "))
hora = (float(segundos / 3600))
print(f"El resultado de {segundos} segundos pasados a horas es: {hora}")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

multi = int(input("Ingrese el numero que desea multiplicar: "))
print(f"{multi} x 1 = {multi * 1}")
print(f"{multi} x 2 = {multi * 2}")
print(f"{multi} x 3 = {multi * 3}")
print(f"{multi} x 4 = {multi * 4}")
print(f"{multi} x 5 = {multi * 5}")
print(f"{multi} x 6 = {multi * 6}")
print(f"{multi} x 7 = {multi * 7}")
print(f"{multi} x 8 = {multi * 8}")
print(f"{multi} x 9 = {multi * 9}")
print(f"{multi} x 10 = {multi * 10}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
suma = num1 + num2
print(f"El resultado de la suma es: {suma}")
resta = num1 - num2
print(f"El resultado de la resta es: {resta}")
multiplicacion = num1 * num2
print(f"El resultado de la multiplicacion es: {multiplicacion}")
division = num1 / num2
print(f"El resultado de la division es: {division}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
resultado = peso / (altura ** 2)
print(f"Su indice de masa corporal es de {resultado}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahr = (9/5) * celsius + 32
print(f"La temperatura de {celsius} grados celsius a Fahrenheit es de: {fahr}")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
suma = num1 + num2 + num3
prom = suma / 3
print(f"El promedio de las notas es de: {prom}")

a = 10
b = 3.0
c = a * b
d = a + b
print(f"c={c} b={d}")