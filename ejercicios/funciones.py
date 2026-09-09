#CASO APLICADO - PRACTICA DE FERRETERIS

print("----------------- FERRETERIA DON PABLO -----------------------")
print(" ")

product_name= str(input("Ingrese el nombre del producto: "))
product_amount= int(input("Ingrese la cantidad que lleva: "))
product_price= float(input("Precio: "))

def subtotal(product_price, product_amount):
    return product_amount*product_price

print(subtotal)