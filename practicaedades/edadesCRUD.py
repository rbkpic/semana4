edades =[]
def agregar(edad):
    if edad >= 0:
        edades.append(edad)

def mostrar():
    return edades

def evaluaredades():
    for edad in edades:
        if edad < 6:
            categoria = "INFANTE"
            print(f"{edad} años es {categoria}")
        elif edad < 18:
            categoria = "NIÑO"
            print(f"{edad} años es {categoria}")
        else:
            categoria = "ADULTO"
            print(f"{edad} años es {categoria}")
            
        