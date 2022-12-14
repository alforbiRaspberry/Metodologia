# Ejercicio 1 - Condicionales

import time
import os

def menu():
    print("""
Programas condicionales:
1. Ejercicio 1 - Hola a todos
2. Ejercicio 2 - Huerto de zanahorias
3. Ejercicio 3 - Figuras geométricas
4. Ejercicio 4 - Series numéricas
5. Ejercicio 5 - Clasificacion de letras
6. Ejercicio 6 - Es numérico
7. Ejercicio 7 - Invertir nombre
8. Ejercicio 8 - Cuenta regresiva
9. Ejercicio 9 - Simulación de calificaciones
10. Ejercicio 10 - Clave y valor
11. Ejercicio 11 - Correo Electronico valido
""")
    
    
def hola_a_todos():
    print("Algoritomo que saluda a todos 10 veces")
    for i in range(10):
        print("Hola a todos")


def huerto_zanahorias():
    print("Ayuda al abuelo Rodolfo a sembrar zanahorias")
    print("Cuantas zanahoras desas sembrar [1 - 1000]:")
    zanahorias = int(input())

    if zanahorias >= 1 and zanahorias <= 1000:
        for i in range(zanahorias):

            if i != 0 and i % 10 == 0:
                print("")
            print("*", end="")
        print("")
    else:
        print("Error. Valor fuera de rango [1-1000]")

def figuras_geometricas():
    print("----------------------------------")
    print("""
           1. Cuadrado
           2. Triangulo
           3. Rectangulo
----------------------------------
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
    a = 5
    print("Serie Ascendente")
    for i in range(1,100+1):
        if a != 500:
            print(a, ", ", end="")
        else:
            print(a, end="")
        a += 5
        if a % 100 == 0:
            print("")
    print("")

    a = 500
    print("Serie Descendente")
    for i in range(1,100+1):
        if a != 5:
            print(a, ", ", end="")
        else:
            print(a, end="")
        a -= 5
        if a % 100 == 0:
            print("")
    print("")

    aux1 = 1
    aux2 = 0
    for i in range(1, 23):
        if i != 22: #limite - 1
            print(aux1 + aux2, ", ", end="")
        else:
            print(aux1 + aux2)
        aux1 = aux1 + aux2
        aux2 = aux1 - aux2
    print()


    print("Ingresa el factorial que deseas imprimir")
    factorial = int(input())
    acumulador = factorial
    for i in range(factorial):
        if factorial != 1:
            print(factorial, "x ", end="") #Imprime comas excepto en el último valor
        else:
            print(factorial, end="") #imprime comas
        if i != 0: #no asigna el producto de acumulador por factorial en la primera iteración
            acumulador = acumulador * factorial
        factorial -= 1
    print(" =", acumulador, end="")
    print("") #Salto de linea

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
        if c[i] < '0' or c[i] > '9':
        #if ord(c[i]) < 48 or ord(c[i]) >57:
            return 1
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

    while (horas > 0 or minutos > 0 or segundos > 0):
        print(horas, ":", minutos, ":", segundos)
        #os.system("clear")
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
    print("Ingrese el codigo en cadena. [Recuerda finalizar la cadena con '|']:")
    cadena = input()
    calificacion_real = 0.0
    i = 0
    while i < len(cadena):
        num_alumno = ""
        calificacion = ""
        while cadena[i] != '=':
            num_alumno += cadena[i]
            i = i + 1
        i += 1
        while cadena[i] != '|':
            calificacion += cadena[i]
            i += 1
        i += 1
        calificacion_real = float(calificacion)
        if calificacion_real == 1:
            calificacion = "uno"
        elif calificacion_real == 2:
            calificacion = "dos"
        elif calificacion_real == 3:
            calificacion = "tres"
        elif calificacion_real == 4:
            calificacion = "cuatro"
        elif calificacion_real == 5:
            calificacion = "cinco"
        elif calificacion_real == 6:
            calificacion = "seis"
        elif calificacion_real == 7:
            calificacion = "siete"
        elif calificacion_real == 8:
            calificacion = "ocho"
        elif calificacion_real == 9:
            calificacion = "nueve"
        elif calificacion_real == 10:
            calificacion = "diez"

        print("EL estudiante con clave ", num_alumno, " tiene una calificacion de ", calificacion)

def verificar_email():
    while email_correcto(input("Ingresa la dirección de correo:")):
        print("Dirección de correo no valido. Vuelva a intentarlo.")
    print("Direccion de correo valida.")

def email_correcto(email):
    i = 0
    nombre_usuario = ""
    dominio = ""
    tipo = ""

    while i < len(email) and email[i] != '@':
        nombre_usuario = nombre_usuario + email[i]
        i += 1
    if i == len(email):
        print(nombre_usuario)
        return 1
    if len(nombre_usuario) < 3:
        return 1
    #if email[i] != '@':
    #    return 1
    i += 1
    while i < len(email) and email[i] != '.':
        dominio += email[i]
        i += 1
    if i == len(email):
        print(dominio)
        return 1
    if dominio != "gmail" and dominio != "outlook" and dominio != "hotmail":
        print(dominio)
        return 1
    #if email[i] != '.':
    #    return 1
    i += 1
    while i < len(email):
        tipo += email[i]
        i += 1
    if tipo != "com" and tipo != "es":
        print(tipo)
        return 1
    else:
        print(nombre_usuario,"@", dominio, ".", tipo)
        return 0

def prueba_for():
    variab = 10
    for i in range (variab):
        print(i)
        variab = 4

    entero = int("0009")
    print(entero)






# main del programa
salir = 0
while salir == 0:
    print("Ingrese el programa que desee ejecutar [1 - 11]. Presione 0 para ver las opciones")
    opcion = int(input())
    while opcion == 0:
        menu()
        print("Ingrese el programa que desee ejecutar (1 - 11). Presione 0 para ver las opciones")
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
    elif opcion == 10:
        clave_valor()
    elif opcion == 11:
        verificar_email()
    else:
        print("Error. Ingrese un valor valido.")
    print("Deseas ejecutar otro programa [y/n]:")
    if str.lower(input()) == "n":
        salir = 1
