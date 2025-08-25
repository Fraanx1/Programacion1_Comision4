semana = ["lunes","martes","miercoles","jueves","viernes"]

semana1 = input("Ingrese el dia y la fecha en formato DD/MM: ")

#Divide las partes del dia con la fecha completa

partes = semana1.split(",")

dia_semana = partes[0].strip().lower()
fecha = partes[1].strip()

#Divide la fecha del dia con el mes
fecha_partes = fecha.split("/")
dia = int(fecha_partes[0])
mes = int(fecha_partes[1])

#Busca si hay algun error en la fecha
if dia < 1 or dia > 31:
    print("Dia incorrecto")

if mes < 1 or mes > 12:
    print("Mes incorrecto")

print(semana1)

#El codigo busca si el dia es lunes, martes, miercoles, jueves o viernes y hace sus respectivas preguntas
if dia_semana != 'jueves' and dia_semana != 'viernes':
    exam = input("¿Hubo examenes?(Responder con Si o No)").lower()
    if exam == 'si':
        aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
        desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
        porcentaje = aprobados / (aprobados + desaprobados) * 100
        print(f"El porcentaje de aprobados es de: {porcentaje}")
else:
    if dia_semana == 'jueves':
        asistencia = int(input("Ingrese el porcentaje de asistencia:"))
        if asistencia > 50:
            print("Asistio la mayoria")
        else:
            print("No asistio la mayoria")
    if dia_semana == 'viernes':
        if dia == 1 and mes == 1 or mes == 7:
            print("Comienzo del nuevo ciclo")
            cantidad_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            arancel = int(input("Ingrese el arancel por alumno: "))
            print(f"El arancel total entre los {cantidad_alumnos} alumnos, es de ${cantidad_alumnos * arancel}")
        else:
            print("No es inicio del ciclo")




    
