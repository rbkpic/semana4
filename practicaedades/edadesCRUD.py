edades =[]

def agregar(usuario):
    if usuario < 0 or usuario >= 50:
        print("Ingrese edad válida")
    else:
        edades.append(usuario)



def mostrar():
    return edades

def evaluaredades():
    for edad in edades:
        if edad < 6:
            categoria = "INFANTE"
            print(f"{edad} años es {categoria}")
        elif edad < 12:
            categoria = "NIÑO"
            print(f"{edad} años es {categoria}")
        elif edad < 19:
            categoria = "ADOLESCENTE"
            print(f"{edad} años es {categoria}")
        elif edad < 45:
            categoria = "JOVEN"
            print(f"{edad} años es {categoria}")
        elif edad < 60:
            categoria = "ADULTO"
            print(f"{edad} años es {categoria}")
        else:
            categoria = "ADULTO MAYOR"
            print(f"{edad} años es {categoria}")

def maxymin():
    edadmayor = max(edades)
    edadmenor = min(edades)
    print(f"La edad mayor es: {edadmayor}")
    print(f"La edad menor es: {edadmenor}")
        