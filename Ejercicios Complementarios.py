#1. Crea una variable llamada "numero1" y asígnale un número entero de tu elección.
numero1 = 10
numero2 = 5.5

#3. Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2".
suma = numero1 + numero2
print(suma)

#4. Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para
#multiplicación y otra para división. Imprime estas variables.
multi = numero1 * numero2
print(multi)

division = numero1 / numero2
print(division)

#5. Crea una variable llamada "nombre" y asígnale tu nombre como valor
nombre = "Franco"

#6. Crea una variable llamada "precio" y asígnale un valor decimal que represente el
#precio de un artículo ficticio.
#7. Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale
#un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le
#quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al
#100% y el valor 0 al 0%
precio = 100.0
descuento = 0.10
precio_final = precio - (precio * descuento)
print(precio_final)

#9. Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu
#elección. Qué sea un string
#10. Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas
#a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de
#Python.
cadena = "Hola Mundo"
longitud = len(cadena)
print(longitud)

#11. Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y
#conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo
#mismo
precio1 = int(99.9)
print(precio1)

#12. Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas
#en una tercera variable llamada "nombre_completo", el nombre y el apellido con un
#espacio entre medio. Puedes usar libremente la forma de concatenación que quieras.
nombre1 = "Franco"
apellido = " Rios"
Nombre_Apellido = print(nombre1 + apellido)

#13. Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10.
edad = 19 + 5 - 10
print(edad)

#14. Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y
#centímetros. Por ejemplo: 1.83. Multiplícala por 4 y luego divídela en 3.
altura = 1.73 * 4 / 3
print(altura)

#15. Crea una variable que contenga tu nombre completamente en mayúsculas. Después
#transfórmalo todo en minúsculas con algún método o función de Python.
nombre_mayus = "FRANCO"
nombre_minus = print(nombre_mayus.lower())

#16. Por último, con la variable con el nombre en mayúsculas, aplica un método parecido
#para que se transforme todo en minúsculas excepto la primera letra.
nombre_com = print(nombre_mayus.capitalize())

