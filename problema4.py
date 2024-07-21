def ingresar_datos_alumno():
    alumnos = []
    notas = []
    
    nombre = imput("Ingrese el nombre del alumon: ")
    
    for i in range(1,3):
        nota = float(input(f"Ingrese la nota {i} para {nombre}: "))
        notas.append(nota)

    alumnos.append({"Alumno": nombre, "Notas": notas})

    return alumnos

def mostrar_lista(n_alumnos):
    print("Listado de alumonos")
    for x in n_alumnos:
        nombre = x["Alumno"]
        notas = x["Notas"]
        print(f"Alumno: {nombre}, Notas: {notas}")

