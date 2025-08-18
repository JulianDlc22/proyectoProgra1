from unittest import case


class Tienda:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def ver_info(self):
        return f"Codigo: {self.codigo} - Nombre del Producto: {self.nombre} - Categoria: {self.categoria} - Precio: Q.{self.precio} - Stock: {self.stock} unidades "

#Creo los quick sort para ordenarlo
def quick_sort_nombre(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x[1].nombre < pivote[1].nombre]
    iguales = [x for x in lista if x[1].nombre == pivote[1].nombre]
    mayores = [x for x in lista[1:] if x[1].nombre > pivote[1].nombre]

    return quick_sort_nombre(menores) + iguales + quick_sort_nombre(mayores)

def quick_sort_precio(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x[1].precio < pivote[1].precio]
    iguales = [x for x in lista if x[1].precio == pivote[1].precio]
    mayores = [x for x in lista[1:] if x[1].precio > pivote[1].precio]

    return quick_sort_precio(mayores) + iguales + quick_sort_precio(menores)

def quick_sort_stock(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x[1].stock < pivote[1].stock]
    iguales = [x for x in lista if x[1].stock == pivote[1].stock]
    mayores = [x for x in lista[1:] if x[1].stock > pivote[1].stock]

    return quick_sort_stock(mayores) + iguales + quick_sort_stock(menores)

class GestionTienda:
    def __init__(self):
        self.Tienda = {}

    def agregar_producto(self):

        print("--Sistema de Ingreso de Productos--")

        rango = int(input("Cuantos Productos desea Registrar?: "))

        for i in range(rango):

            print(f"\nProducto No.{i+1}")

            while True:
                codigo = input("Codigo del Producto: ")
                if codigo in self.Tienda:
                    input("Codigo ingresado ya en exitencia, presione para volver a Ingresarlo")
                    continue
                break

            nombre = input("Nombre del Producto: ")
            categoria = input("Categoria del Producto: ")

            while True:
                try:
                    precio = float(input("Precio del Producto: "))
                    if precio < 0:
                        input("error- precio no valido, presione para volver a Ingresarlo")
                        continue  # vuelve al inicio del while para pedir de nuevo el precio.

                    break  # se ejecuta si el precio es correcto y te saca del while
                except ValueError:
                    input("error- precio no valido, presione para volver a Ingresarlo")

            while True:
                try:
                    stock = int(input("Stock del Producto: "))
                    if precio <= 0:
                        input("error- stock no valido, presione para volver a Ingresarlo ")
                        continue

                    break
                except ValueError:
                    input("error- Stock no valido, presione para volver a Ingresarlo")

        self.Tienda[codigo] = Tienda(codigo, nombre, categoria, precio, stock)
        print("Producto Agregado Exitosamente...")

    def lista_productos(self):
        if not self.Tienda:
            print("No hay productos ingresados")
            return
        print("\nLista de Productos:")
        try:
            lista_tienda = list(self.Tienda.items())
            opcion_orden = int(input("Como desea ver el orden de los productos (1.Nombre del Producto, 2. Precio del Producto, 3. Stock del Producto) : "))
            if opcion_orden == 1:
                orden_nombre = quick_sort_nombre(lista_tienda)
                for codigo, informacion in orden_nombre:
                    print(f"Codigo: {codigo} - Nombre: {informacion.nombre}, Precio: {informacion.precio}, Stock: {informacion.stock}")
            elif opcion_orden == 2:
                orden_precio = quick_sort_precio(lista_tienda)
                for codigo, informacion in orden_precio:
                    print(f"Codigo: {codigo} - Nombre: {informacion.nombre}, Precio: {informacion.precio}, Stock: {informacion.stock}")
            elif opcion_orden == 3:
                orden_stock = quick_sort_stock(lista_tienda)
                for codigo, informacion in orden_stock:
                    print(f"Codigo: {codigo} - Nombre: {informacion.nombre}, Precio: {informacion.precio}, Stock: {informacion.stock}")
            else:
                print("error- La opcion que escogio no esta en las que se tiene disponible, volvera al menu")
        except ValueError:
            input("error- opcion no valido, presione enter para continuar ")
    def buscar_producto(self):
        pass
    def modificar_producto(self):
        pass
    def eliminar_producto(self):
        pass



registro = GestionTienda()
while True:
    print("MENU")
    print("1. Agregar Producto")
    print("2. Listar Productos")
    print("3. Buscar Producto")
    print("4. Modificar o Eliminar Producto")
    print("5. Salir")
    try:
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                registro.agregar_producto()
            case 2:
                registro.lista_productos()
            case 3:
                pass
            case 4:
                pass
            case 5:
                print("Gracia por utilizar el programa")
                print("Saliendo...")
                break
    except ValueError:
        input("error- opcion no valido, presione enter para continuar ")

