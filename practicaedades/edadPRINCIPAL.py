import edadesCRUD

def leeredad():
    print("Dime la edad: ")
    edad =int(input())
    edadesCRUD.agregar(edad)

def menu():
    print("""
    1. Ingresar edad
    2. Mostrar edades
    3. Evaluar edad
    0. Salir
    Digita una opción válida:
    """)
    opcion=int(input())
    return 

def main():
    while True:
        op = menu()
        if op ==1:
            leeredad()
        elif op==2:
            print(edadesCRUD.mostrar())
        elif op==3:
            edadesCRUD.evaluaredades()
        elif op==0:
            print("Adios...")
        else:
            print("Opcion invalida...")

main()