# Ejercicio 1 - Condicionales

import time
import os

def hola_a_todos():
    for i in range(10):
        print("Hola a todos")


def huerto_zanahorias():
    print("Ayuda al abuelo Rodolfo a sembrar zanahorias")
    print("Cuantas zanahoras desas sembrar [1 - 1000]:")
    zanahorias = int(input())

    if zanahorias >= 1 and zanahorias <= 1000:
        for i in range(zanahorias):
            print("*", end="")
            if i != 0 and i % 9 == 0:
                print("")
        print("")

def figuras_geometricas():
    print("----------------------------------")
    print("""
           1. Cuadrado
           2. Triangulo
           3. Rectangulo
""")
    print("\nSeleccione una opción: ")
    figura = int(input())
    print("Ingrese el numero de filas de la figura: ")
    longitud = int(input())    

    if figura == 1:
        for i in range(longitud):
            for j in range(longitud):
                print("*  ", end="")
            print("")
    elif figura == 2:
        aux = longitud
        for i in range(longitud):
            for j in range(aux):
                print("*  ", end="")
            aux = aux - 1
            print("")
    elif figura == 3:
        for i in range(int(longitud / 2)):
            for j in range(int(longitud)):
                print("*  ", end="")
            print("")
    else:
        print("Opcion no valida")

def series():
    for i in range(10):
        print(i, ", ", end="")
        #i = i + 4
        print("")

    for i in range(-1):
        print(i)
        i = i - 4

    aux1 = 1
    aux2 = 0
    for i in range(7):
        print(aux1 + aux2, ", ", end="")
        aux1 = aux1 + aux2
        aux2 = aux1 - aux2
        print(i)
    print()


    print("Ingresa el factorial que deseas imprimir")
    factorial = int(input())
    acumulador = 0
    for i in range(factorial):
        print(factorial, " x ", factorial - 1, end="=")
        acumulador = acumulador + factorial * (factorial - 1)
        i = i - 1
        factorial = factorial - 1

def clasificacion_letras():
    print("Ingresa cualquier cosa: ")
    entrada = input()

    vocales = 0
    consonantes = 0
    espacio_blanco = 0
    caracter_extrano = 0

    entrada = entrada.lower()

    for i in range(len(entrada)):
        #print(ord(entrada[i])) esta linea imprime el codigo ascci de el indice i de la cadena
        if entrada[i] == 'a' or entrada[i] == 'e' or entrada[i] == 'i' or entrada[i] == 'o' or entrada[i] == 'u':
            vocales += 1
        elif ord(entrada[i]) >= 97 and ord(entrada[i]) <= 122:
            consonantes += 1
#            if entrada(i) == 'a' or entrada(i) == 'e' or entrada(i) == 'i' or entrada(i) == 'o' or entrada(i) == 'u':
#               vocales = vocales + 1
#         else:
#               onsonantes =+ 1
        elif entrada[i] == " ":
            espacio_blanco += 1
        else:
            caracter_extrano += 1

    print("Vocales:", vocales)
    print("Consonantes:", consonantes)
    print("Espacios:", espacio_blanco)
    print("Simbolos:", caracter_extrano)

def is_numeric(c):
    for i in range(len(c)):
        if c[i] == " " or c[i] == None:
            return 1
        if c[i] < 0 and c[i] > 9:
            return 1
        else:
            return 0

def es_numerico():
    print("Ingresa un valor: ")
    cadena = input()


    alpha_characters = 0
    i = 0
    #while(alpha_characters != 1 and i < len(cadena)):
     #   if not(ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57):
      #      alpha_characters += 1
       # i = i + 1

    #if alpha_characters:
     #   print("La cadena no es numerica")
    #else:
     #   print("La cadena es numerica")
    if is_numeric(cadena):
        print("La cadena no es numerica")
    else:
        print("La cadena es numerica")

def invertir_cadena():
    print("Programa que invierte cadenas")
    print("Ingresa algo:")
    cadena = input()

    if cadena != None and len(cadena) > 1:
        new_cadena = cadena
        print("La cadena invertida es: ", end="")
        for i in range(len(cadena)):
            print(cadena[(len(cadena) - 1) - i], end="")
        print("")
    else:
        print("La cadena ingresada no cumple los requisitos")

def cuenta_regresiva():
    print("Temporizador digital")
    print("Ingrese las horas:")
    horas = int(input())
    print("Ingrese los minutos")
    minutos = int(input())
    print("Ingrese los segundos")
    segundos = int(input())

    while (horas > 0 or minutos > 0 or segundos >= 0):
        print(horas, ":", minutos, ":", segundos)
        os.system("clear")
        time.sleep(1)
        if minutos == 0 and segundos == 0:
            horas -= 1
            minutos = 60
            segundos = 60
        if segundos == 0:
            minutos -= 1
            segundos = 60
        segundos -= 1
    print("RING RING RING RING")

def simulacion_calificacioneS():
    print("Programa que captura 20 calificaciones e imprime la nota más alta,", end="")
    print("la más baja y el promedio")
    print("")
    cal_mayor = 0
    cal_menor = 10
    promedio = 0
    cadena_calificaciones = ""

    for i in range(20):
        print("Ingresa la calificación ", i + 1, ":")
        calificacion = float(input())
        cadena_calificaciones += str(calificacion)
        cadena_calificaciones += ", "
        if calificacion < cal_menor:
            cal_menor = calificacion
        if calificacion > cal_mayor:
            cal_mayor = calificacion
        promedio += calificacion
    print("")
    promedio = promedio / 20

    print(cadena_calificaciones)
    print("La nota mayor es: ", cal_mayor)
    print("La nota menor es: ", cal_menor)
    print("EL promedio es: ", promedio)

def clave_valor():
    print("Programa que captura una cadea de codigo y lo transforma en información de calificaciones")
    print("Ingrese el codigo en cadena:")
    cadena = input()

    index = ""
    num_estudiante = ""
    for i in range(len(cadena)):
        if cadena[i] == '=':
            num_estudiante = cadena[i]









# main del programa
salir = 0
while salir == 0:
    print("Ingrese el programa que desee ejecutar [0 - 0]. Presione 0 para ver las opciones")
    opcion = int(input())
    while opcion == 0:
        print("Ingrese el programa que desee ejecutar (0 - 0). Presione 0 para ver las opciones")
        opcion = int(input())
    if opcion == 1:
        hola_a_todos()
    elif opcion == 2:
        huerto_zanahorias()
    elif opcion == 3:
        figuras_geometricas()
    elif opcion == 4:
        series()
    elif opcion == 5:
        clasificacion_letras()
    elif opcion == 6:
        es_numerico()
    elif opcion == 7:
        invertir_cadena()
    elif opcion == 8:
        cuenta_regresiva()
    elif opcion == 9:
        simulacion_calificacioneS()
    else:
        print("Error. Ingrese un valor valido.")
    print("Deseas ejecutar otro programa [y/n]:")
    if str.lower(input()) == "n":
        salir = 1
