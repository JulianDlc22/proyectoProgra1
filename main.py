class Tienda:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def VerInfo(self):
        return f"Codigo: {self.codigo} - Nombre del Producto: {self.nombre} - Categoria: {self.categoria} - Precio: Q.{self.precio} - Stock: {self.stock} unidades "


#Creo los quick sort para ordenarlo
def quick_sort_nombre(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort_nombre(menores)+iguales+quick_sort_nombre(mayores)

def quick_sort_precio(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort_precio(menores)+iguales+quick_sort_precio(mayores)

def quick_sort_stock(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort_stock(menores)+iguales+quick_sort_stock(mayores)

class GestionTienda:
    def __init__(self):
        self.Tienda = {}

    def AgregarProducto(self):

        print("--Sistema de Ingreso de Productos--")

        codigo = input("\nCodigo del Producto: ")
        if codigo in self.Tienda:
            input("Codigo ingresado ya en exitencia, presione enter para continuar")
            return

        nombre = input("Nombre del Producto: ")
        categoria = input("Categoria del Producto: ")

        while True:
            try:
             precio = float(input("Precio del Producto: "))
             if precio < 0:
                 input("error- precio no valido, presione enter para continuar ")
                 continue #vuelve al inicio del while para pedir de nuevo el precio.

             break #se ejecuta si el precio es correcto y te saca del while
            except ValueError:
                input("error- precio no valido, presione enter para volver a ingresarlo")

        while True:
            try:
             stock = int(input("Stock del Producto: "))
             if precio <=0:
                 input("error- stock no valido, presione enter para continuar ")
                 continue

             break
            except ValueError:
                input("error- Stock no valido, presione enter para volver a ingresarlo")

        self.Tienda[codigo] = Tienda(codigo, nombre, categoria, precio, stock)
        print("Producto Agregado Exitosamente...")

    def ListaProductos(self):
        print("\nLista de Productos:")
        try:
            opcion_orden = int(input("Como desea ver el orden de los productos: (1.Nombre del Producto, 2. Precio del Producto, 3. Stock del Producto)"))
            if opcion_orden == 1:
                pass
            elif opcion_orden == 2:
                pass
            elif opcion_orden == 3:
                pass
            else:
                print("error- La opcion que escogio no esta en las que se tiene disponible, volvera al menu")
        except ValueError:
            input("error- opcion no valido, presione enter para continuar ")
    def BuscarProducto(self):
        print("")




registro = GestionTienda()

registro.AgregarProducto()