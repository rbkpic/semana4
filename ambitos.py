# Variable global
nombre_empresa = "UAM"

def mostrar_empresa():
  print(nombre_empresa)

mostrar_empresa()

def calcular_total():
  total = 250

calcular_total()
print(total)
#porque total fue declarada dentro de una funcion y deja de existir una vez se ejecuta la funcion.
contador = 0

def incrementar_contador():
  global contador 
  contador += 1


print("Valor inicial:", contador) 
incrementar_contador()
incrementar_contador()
print("Valor modificado:", contador)  