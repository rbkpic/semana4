#registro de estudiantes
"""
Datos a registrar: cif, nombres, apellidos, carrera, promedio
"""

notas =[]
def agregar(nota):
    notas.append(nota)

def mostrar():
    return notas

def evaluarnotas():
    for nota in notas:
        if nota>=70:
            print(f"{nota},  es parobado")
        else:
            print(f"{nota}, tiene que mejorar")