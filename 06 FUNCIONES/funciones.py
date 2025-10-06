#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo():
    return "Hola Mundo!"

print(imprimir_hola_mundo())

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"¡Hola {nombre}!")

nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta
#función con los valores ingresados.

def informacion_persona(nombre,apellido, edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
informacion_persona(nombre, apellido, edad, residencia)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva
#el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
#Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

from math import pi
def calcular_area_circulo(radio):
    area = (radio**2) * pi
    return area
def calcular_perimetro_circulo(radio):
    perimetro = (2 * pi) * radio
    return perimetro

radio = int(input("Ingrese el radio del círculo: "))
print(f"El area del circulo es de: {calcular_area_circulo(radio)}")
print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio)}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos = int(input("Ingrese la cantidad de segundos: "))
print(segundos_a_horas(segundos))

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

numero = int(input("Ingrese el número que desea ver la tabla de multiplicar: "))
tabla_multiplicar(numero)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    #SUMA:
    print(f"{a} + {b} = {a+b}")
    #RESTA:
    print(f"{a} - {b} = {a-b}")
    #MULTIPLICACIÓN:
    print(f"{a} x {b} = {a*b}")
    #DIVISIÓN:
    print(f"{a} / {b} = {a/b}")

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
operaciones_basicas(a, b)

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / altura**2
    imc = int(imc)
    return imc

peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))
print(calcular_imc(peso, altura))

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fah = (celsius * 1.8) + 32
    fah = int(fah)
    return fah

celsius = float(input("Ingrese los grados que desea pasar: "))
print(f"{celsius_a_fahrenheit(celsius)}°F")

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

def calcular_promedio(num1, num2, num3):
    prom = (num1+num2+num3) / 3
    return prom

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
print(calcular_promedio(num1, num2, num3))

