import crud
def leerdatos():
    print("Dime la nota: ")
    nota =int(input())
    crud.agregar(nota)

def menu():
    print("""
    1. Ingresar nota
    2. Mostrar notas
    3. Evaluar notas
    0. Salir
    Digita una opción válida:
    """)
    opcion=int(input())
    return 

def main():
    while True:
        op = menu()
        if op ==1:
            leerdatos()
        elif op==2:
            print(crud.mostrar())
        elif op==3:
            crud.evaluarnotas()
        elif op==0:
            print("Adios...")
        else:
            print("Opcion invalida...")

main()