#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {"Banana": 1200, "Anana": 2500, "Melon": 3000, "Uva": 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melon"] = 2800
print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.

frutas = list(precios_frutas.keys())
print(frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe

contactos = {}

for i in range(5):
    nombre_contacto = input("Ingrese el nombre del contacto: ").strip().capitalize()
    numero_contacto = int(input(f"Ingrese el número del contacto {nombre_contacto}: "))
    contactos[nombre_contacto] = numero_contacto

buscar_nombre = input("Ingrese el nombre del contacto que busca: ").strip().capitalize()

if buscar_nombre in contactos:
    print(f"El número del contacto {buscar_nombre} es {contactos[buscar_nombre]}.")
else:
    print("Ese contacto no existe.")

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ").strip().lower()
palabras = frase.split()
palabras_unicas = set(palabras)
print(palabras_unicas)

cantidad_palabras = {}
for i in palabras:
    if i in cantidad_palabras:
        cantidad_palabras[i] += 1
    else:
        cantidad_palabras[i] = 1

print(f"La cantidad de veces que se repiten las palabras: {cantidad_palabras}")

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

alumnos_dic = {}

for i in range(3):
    alumnos = input("Ingrese el nombre del alumno: ").strip().capitalize()

    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} del alumno {alumnos}: "))
        notas.append(nota)
    alumnos_dic[alumnos] = tuple(notas)

for alumnos, notas in alumnos_dic.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumnos} tiene un promedio de: {promedio}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {"Franco","Fabrizio","Maximo","Santino","Juan Manuel"}
parcial2 = {"Thiago","Maximo","Franco","Marcelo","Fabrizio"}

ambos = parcial1 & parcial2
print(f"{ambos}, aprobaron ambos parciales.")

solo_uno = parcial1 ^ parcial2
print(f"{solo_uno} aprobaron 1 de 2 parciales.")

al_menos = parcial1 | parcial2
print(f"{al_menos} aprobaron al menos un parcial.")

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

productos = {"Yerba": 25,"Manteca": 13,"Dulce de leche": 18}

while True:
    print("1. Consultar el stock de un producto.")
    print("2. Agregar unidades al stock de un producto.")
    print("3. Agregar un producto.")
    print("4. Lista completa de los productos con su stock.")
    print("5. Salir")
    opcion = input("Ingrese una opción: ")

    match opcion:
        case "1":
            consultar = input("Ingrese el nombre del producto que desea consultar: ").strip().capitalize()
            if consultar in productos:
                print(f"El stock del producto {consultar} es de {productos[consultar]} unidades.")
            else:
                print("Ese producto no existe, vuelva a ingresar.")
        case "2":
            stock = input("Ingrese el nombre del producto que desea cambiar el stock: ").strip().capitalize()
            if stock in productos:
                try:
                    cantidad = int(input("Ingrese la cantidad de unidades que va a agregar: "))
                    if cantidad > 0:
                        productos[stock] += cantidad
                        print(f"Se agregaron {cantidad} unidades al stock del producto {productos[stock]}.") # ¿Por que me da el stock y no el producto? Al poner .keys() tampoco deja
                    else:
                        print("ERROR. Ingrese un número positivo.")
                except ValueError:
                    print("ERROR. Ingrese un número.")
            else:
                print("Ese producto no existe, vuelva a ingresar.")
        case "3":
            agregar = input("Ingrese el nombre del producto que desea agregar: ").strip().capitalize()
            if agregar in productos:
                print("Ese producto ya fue añadido anteriormente, ingrese otro.")
            else:
                try:
                    nuevo_stock = int(input("Ingrese las unidades que tiene ese producto para agregar: "))
                    if nuevo_stock >= 0:
                        productos[agregar] = nuevo_stock
                    else:
                        print("Por favor, ingrese un número positivo.")
                except ValueError:
                    print("ERROR. Ingrese un número valido.")
        case "4":
            for prod, stock in productos.items():
                print(f"{prod}: {stock} unidades.")
        case "5":
            print("Saliendo del programa...")
            break

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

agenda = {}

dias = int(input("Ingrese la cantidad de días que tiene eventos: "))
for i in range(dias):
    dia = input("Ingrese el día que tiene el evento: ").strip().capitalize()
    hora = input("Ingrese el horario en el que tiene el evento: ")
    evento = input("Ingrese que evento tiene ese día: ").strip().capitalize()
    agenda[(dia,hora)] = evento
print(list(agenda.keys()))

dia_buscar = input("Ingrese el día para saber su actividad: ").strip().capitalize()
hora_buscar = input("Ingrese el horario para saber su actividad: ")
if (dia_buscar, hora_buscar) in agenda:
    print(f"El evento que tiene el día {dia_buscar} en el horario {hora_buscar} es {agenda[dia_buscar,hora_buscar]}.")
else:
    print("No tiene ninguna actividad en ese día/horario.")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
capitales = {}
print(original)
for pais, capital in original.items():
    capitales[capital] = pais
print(capitales)