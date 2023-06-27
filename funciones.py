import os
import numpy as np
import colorama as c
import msvcrt
import random

#Arreglo de producto
alumnos = np.empty([10,7], object)

def limpiar_pantalla():
    print("Presione una tecla para continuar")
    msvcrt.getch()
    os.system('cls')

def printr(texto):
    print(f"{c.Fore.RED}{texto}{c.Fore.RESET}")
def printam(texto):
    print(f"{c.Fore.YELLOW}{texto}{c.Fore.RESET}")
def printv(texto):
    print(f"{c.Fore.GREEN}{texto}{c.Fore.RESET}")
def printaz(texto):
    print(f"{c.Fore.BLUE}{texto}{c.Fore.RESET}")

def printtitulo(texto):
    print(f"""
   {c.Fore.YELLOW}-------------------------------{c.Fore.RESET}
                {c.Fore.BLUE}{texto}{c.Fore.RESET}
   {c.Fore.YELLOW}-------------------------------{c.Fore.RESET}
    """)

def menu():
    printtitulo("San Charlis")
    printam("""
    1) Registrar
    2) Buscar
    3) Imprimir Certificados
    4) Salir
    """)

def validar_opcion():
    while True:
        try:
            opcion=int(input("Por favor ingrese una opcion:"))
            if opcion>=1 and opcion<=4:
                return opcion
            else:
                printr("Por favor ingrese una opción valida")
        except:
            printr("Error de sistema!! , Por favor ingrese solo numeros enteros")


def buscar():
    pass

def validar_rut(rut):
    for i in range(10):
        if alumnos[i,0]==rut:
            return i
        else:
            return -1

def validar_nombre():
    while True:
        nombre=input("Ingrese nombre:")
        try:
            if len(nombre)>=2 and len(nombre)<=30:
                return nombre
            else:
                printr("Por favor ingrese un nombre valido")
        except:
            printr("Error de sistema")

def validar_edad():
    while True:
        try:
            edad=int(input("Ingrese edad del alumno:"))
            if edad>=4:
                return edad
            else:
                printr("Por favor ingrese una edad valido")
        except:
            printr("Por favor ingrese solo numeros enteros")

def validar_genero():
    genero=str(input("Ingrese genero del alumno F/M:")).upper()
    if genero=="F" or genero=="M":
        return genero
    else:
        printr("Por favor ingrese un genero valido")

def validar_promedio():
    while True:
        try:
            promedio=float(input("Ingrese promedio del alumno:"))
            if promedio>=1.0 and promedio<=7.0:
                return promedio
            else:
                printr("Por favor ingrese promedio en formato 1.0 - 7.0")
        except:
            printr("Error de sistema")
def validar_fecha():
    while True:
        try:
            fechamatricula=input("Ingrese fecha de matricula del alumno:")
            if len(fechamatricula)>6:
                return fechamatricula
            else:
                printr("Por favor ingrese una fecha valida")
        except:
            printr("Error de sistema")

def validar_nombreapoderado():
    while True:
        try:
            nombreapoderado=input("Ingrese nombre del apoderado:").capitalize()
            if len(nombreapoderado)>=2:
                return nombreapoderado
            else:
                printr("Por favor ingrese una nombre valido")
        except:
            printr("Error de sistema")

def registrar(rut,nombre,edad,genero,promedio,fechamatricula,nombreapoderado):
    while True:
        if None in alumnos: #Validar espacio disponible
            if validar_rut(rut)==-1: #Validamos que el codigo no se repita
                for i in range(10):
                    if alumnos[i,0]==None:
                        alumnos[i,0]=rut
                        alumnos[i,1]=nombre
                        alumnos[i,2]=edad
                        alumnos[i,3]=genero
                        alumnos[i,4]=promedio
                        alumnos[i,5]=fechamatricula
                        alumnos[i,6]=nombreapoderado
                        printv(f"Alumno {nombre} REGISTRADO")
                        break
            else:
                printr("Error")
        else:
            printr("Error")


anotacionesalumno=[]
anotacionesalumno.append("Le grita a la profesora")
anotacionesalumno.append("No entra a clases")
anotacionesalumno.append("Se pelea con el compañero")
anotacionesalumno.append("Dice garabatos en sala")
anotacionesalumno.append("Alumno no trabaja en clases")
anotacionesalumno.append("Alumno se queda jugando futbol")
anotacionesalumno.append("Excelente alumno , hace todas las tareas")
anotacionesalumno.append("Excelente alumno , se porta muy bien")
anotacionesalumno.append("Excelente alumno , ayuda siempre a sus compañeros")

certificadonotas=[]
certificadonotas.append("7.0")
certificadonotas.append("6.0")
certificadonotas.append("5.0")
certificadonotas.append("4.0")
certificadonotas.append("3.0")
certificadonotas.append("2.0")
certificadonotas.append("1.0")
certificadonotas.append("5.5")
certificadonotas.append("6.5")


def certificado(rut):
    posicion = validar_rut(rut)
    if posicion>=0:
        printtitulo("CERTIFICADO ANOTACIONES")
        printam(f"""
        rut :{alumnos[posicion,0]}
        nombre      ${alumnos[posicion,1]}
        -----------------------------------------------
        Anotacion del alumno 1: {anotacionesalumno[random.randint(0,9)]}
        Anotacion del alumno 1: {anotacionesalumno[random.randint(0,9)]}
        Anotacion del alumno 1: {anotacionesalumno[random.randint(0,9)]}
        -----------------------------------------------""")

        printtitulo("CERTIFICADO DE NOTAS")
        printam(f"""
        rut :{alumnos[posicion,0]}
        nombre      ${alumnos[posicion,1]}
        -----------------------------------------------
        MATEMATICAS: {certificadonotas[random.randint(0,9)]}
        LENGUAJE: {certificadonotas[random.randint(0,9)]}
        INGLES: {certificadonotas[random.randint(0,9)]}
        HISTORIA: {certificadonotas[random.randint(0,9)]}
        EDUCACION FISICA: {certificadonotas[random.randint(0,9)]}
        -----------------------------------------------""")


        printtitulo("CERTIFICADO DE ALUMNO REGULAR")
        printam(f"""
        rut :{alumnos[posicion,0]}
        nombre      ${alumnos[posicion,1]}
     
        El alumno esta matriculado en colegio presente
        de Puente Alto “San Charlis" desde
        -----------------------------------------------""")

    else:
        printr("ALUMNO NO ENCONTRADO")
