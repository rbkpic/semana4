def aplicar_aumento(precio):
    precio = precio + 100
    print("Precio dentro:", precio)


precio = 500
aplicar_aumento(precio)

print("Precio fuera:", precio)

print(" ")
def agregar_producto(inventario, producto):
    inventario.append(producto)


productos = ["arroz", "aceite"]
agregar_producto(productos, "café")

print(productos)
print(" ")

#PRÁCTICA
def salario_aumento(salario):
    salario+=150
    print("Salario aumentado: ", salario)

salario=800
salario_aumento(salario)

#2
def agregar_venta(ventas):
  ventas.append(150) 
  print("Ventas dentro:", ventas)

lista_ventas = [100, 200]
agregar_venta(lista_ventas)
print("Lista despues de funcion:", lista_ventas)

#En el primer ejercicio, se crea un nuevo valor entero en memoria y asigna el parámetro a esa dirección
#En el segundo se modifica directamente el original sin reasignar la variable.