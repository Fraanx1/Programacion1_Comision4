#1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

with open ("productos.txt","w") as archivo:
    archivo.write("Yerba,2200,15\n")
    archivo.write("Manteca,1500,10\n")
    archivo.write("Dulce de leche,2600,20\n")

#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea 
# la procese con .strip() y .split(",") y muestre los productos en el siguiente formato:

with open ("productos.txt","r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")
        
#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos
# le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) 
#y lo agregue al archivo sin borrar el contenido existente.

nombre1 = input("Ingrese el nombre del producto: ").capitalize().strip()
precio1 = input("Ingrese el precio del producto: ").strip()
cantidad1 = input("Ingrese la cantidad del producto: ").strip()
producto_1 = f"{nombre1},{precio1},{cantidad1}\n"

with open("productos.txt", "a") as archivo:
    archivo.write(producto_1)
    

#Demostrar que se agrego.
with open ("productos.txt","r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.

productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto_actual = {
            "nombre": nombre, "precio": precio, "cantidad": cantidad
        }
        productos.append(producto_actual)
    print(productos)

#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.

buscar = input("Ingrese el nombre del producto que desea buscar: ").strip().capitalize()
prod_encontrado = None
for producto in productos:
    if producto["nombre"] == buscar:
        prod_encontrado = producto
        break
if prod_encontrado:
    nombre = prod_encontrado["nombre"]
    precio = prod_encontrado["precio"]
    cantidad = prod_encontrado["cantidad"]
    print("Producto encontrado:")
    print(f"Nombre: {nombre}")
    print(f"Precio: {precio}")
    print(f"Cantidad: {cantidad}")
else:
    print("ERROR. Ese producto no se encuentra en la lista.")

#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.

with open("productos.txt", "w") as archivo:
    for producto in productos:
        linea = f"{producto["nombre"]},{producto["precio"]},{producto["cantidad"]}\n"
        archivo.write(linea)
#Demostrar que se agregó.
with open ("productos.txt","r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")