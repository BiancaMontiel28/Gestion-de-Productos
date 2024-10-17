productos = []
def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    precio = input("Introduce el precio del producto: ")
    cantidad = input("Introduce la cantidad del producto: ")

    try:
        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })
        print(f"Producto '{nombre}' añadido con éxito.")
    except ValueError:
        print("Error: El precio y la cantidad deben ser números.")

def ver_productos():
    if not productos:
        print("No se han cargado productos en el inventario.")
        return

    print("\nProductos Cargados:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    nombre = input("Introduce el nombre del producto que deseas actualizar: ")

    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            nuevo_cantidad = input("Introduce la nueva cantidad (deja en blanco para no cambiar): ")
            
            if nuevo_cantidad:  
                try:
                    producto["cantidad"] = int(nuevo_cantidad)
                    print(f"Cantidad del producto '{nombre}' actualizada a {producto['cantidad']} con éxito.")
                except ValueError:
                    print("Error: La cantidad debe ser un número.")
            else:
                print("No se ha realizado ningún cambio en la cantidad.")
            return

    print(f"No se encontró el producto '{nombre}'.")

def eliminar_producto():
    global productos

    nombre = input("Introduce el nombre del producto que deseas eliminar: ")

    productos = [producto for producto in productos if producto["nombre"].lower() != nombre.lower()]

    print(f"Producto '{nombre}' eliminado, si existía en la lista.")

def guardar_datos():
    with open('productos.txt', 'w') as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("Datos guardados en 'productos.txt'.")

def cargar_datos():
    try:
        with open('productos.txt', 'r') as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(',')
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })
        print("Datos cargados desde 'productos.txt'.")
    except FileNotFoundError:
        print("No se encontró el archivo 'productos.txt'. Se comenzará con un inventario vacío.")
    except ValueError:
        print("Error en los datos del archivo. Asegúrate de que estén en el formato correcto.")

def menu():
    cargar_datos() 

    while True:
        print("\nMenú:")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()