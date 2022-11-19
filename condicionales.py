#Author: Alan Manuel Villegas Gonzalez
#UTNG
#Desarrollo de Sowftware multiplataforma - GDS0513
#17 November 2022

from random import randrange

def mostrarMenu():
    print("""
    1. Valor Absoluto
    2. Venta de llantas
    3. Descuento al azar
    4. Ecuación Cuadrática
    5. Descuento colegiatura
    """)
def valorAbsoluto(): #Ejercicio 1: Valor absoluto
    print("Programa que calcula el valor absoluto de un numero")
    print("Ingrese un valor: ")
    valor = input()
    valor = float(valor)
    #absoluto = (valor ** 2 ) ** (1/2)
    absoluto = valor
    if valor < 0:
        absoluto = valor * -1

    print("El valor absoluto de ", valor, " es ", absoluto)

#Ejercicio 2: Venta de llantas
def ventaLlantas():
    print("""Programa que calcula el precio total de una venta de llantas
Precio por llanta: $800
Precio por llanta en la compra de 8 o más: $700 
    """)

    print("Ingrese la cantidad de llantas a comprar: ")
    cantidad_llantas = input()

    cantidad_llantas = int(cantidad_llantas)
    if cantidad_llantas >= 8 and cantidad_llantas <= 50:
        precio_total = cantidad_llantas * 700
        print("El total de la compra es de $", precio_total)
    if cantidad_llantas > 0 and cantidad_llantas < 8 :
        precio_total = cantidad_llantas * 800
        print("El total de la compra es de $", precio_total)
    if cantidad_llantas <= 0 or cantidad_llantas > 50 :
        print("La cantidad de llantas no es valido")

#Ejercicio 3: Descuento numero al azar
def descuentoAzar():
    print("Programa que calcula el descuento del monto a pagar")
    print("en base a un numero generado al azar")
    print("(1 - 74) = 15% y (75 - 100) = 20%")
    print ("Ingrese el monto de la compra: ")
    monto_compra = input()
    monto_compra = float(monto_compra)

    if monto_compra > 0:
        aleatorio = randrange(1, 100)
        total = 0.0 #inicializamos la variable por si ninguno de los if se ejecuta
        if aleatorio < 75:
            total = monto_compra - (monto_compra * 0.15)
        if aleatorio >= 75:
            total = monto_compra - (monto_compra * 0.20)

        print("El numero aleatorio fue ", aleatorio)
        print("El total de la compra incluyendo el descuento es de $", total)

    if monto_compra <= 0:
        print("Monto de compra no valido.")

#Ejercicio 4: Ecuacion cuadrarica
def cuadratica():
    print("Programa que calcula las soluciones de una raiz cuadratica")
    print("Ingrese el coeficiente de a: ")
    a = input()
    a = float(a)
    print("Ingrese el coeficiente de b: ")
    b = input()
    b = float(b)
    print("Inrese el coefiente de c: ")
    c = input()
    c = float(c)

    x1 = 0
    x2 = 0
    if a != 0:
        x1 = (-b + (b ** 2 + 4 * a * c) ** (1/2)) / (2 * a)
        x2 = (-b - (b ** 2 + 4 * a * c) ** (1 / 2)) / (2 * a)

        print("El valor de x1 es: ",x1,  end =' ')
        if x1 < 0: print("i")

        print("El valor de x2 es: ",x2,  end =' ')
        if x2 < 0: print("i")

    if a == 0 :
        print("Error, el coeficiente de a diferente de 0")

#Ejercicio 5: Descuento colegiatura
def pagoColegiatura():
    print("Programa que calcula el pago de una colegiatura segun el promedio")
    print("Si el estudiante tiene un promedio de 9 o más se realiza")
    print("un descuento del 30%")

    print("Ingresa el promedio del estudiante: ")
    promedio = input()
    promedio = float(promedio)
    print("Ingresa el monto de la colegiatura")
    precio_colegiatura = input()
    precio_colegiatura = float(precio_colegiatura)
    descuento = 0

    if promedio >= 9 and promedio <= 10:
        descuento = precio_colegiatura * 0.30
        precio_colegiatura = precio_colegiatura - descuento
        print("El descuento por promedio de ", promedio, " es 30% = $", descuento)
        print("El monto total a pagar es $", precio_colegiatura)
    if promedio >= 0 and promedio < 9:
        precio_colegiatura = precio_colegiatura + precio_colegiatura * 0.10
        print("El precio total a pagar es $", precio_colegiatura)
    if promedio < 0 or promedio > 10 or precio_colegiatura <= 0:
        print("Dato invalido")






#Main del programa
opcion = 0
continuar = 'y'
while continuar != 'n':
    print("*******************************************")
    print("  Ingrese el programa que desee ejecutar. Presione 0 para mostrar las opciones")
    opcion = input()
    opcion = int(opcion)
    while opcion == 0:
        mostrarMenu()
        print("  Ingrese el programa que desee ejecutar. Presione 0 para mostrar las opciones")
        opcion = input()
        opcion = int(opcion)

    if opcion == 1:
        valorAbsoluto()
    elif opcion == 2:
        ventaLlantas()
    elif opcion == 3:
        descuentoAzar()
    elif opcion == 4:
        cuadratica()
    else :
        print("Opción no valida. Intente de nuevo.")
    print("Desea ejecutar otro programa? (y/n): ")
    continuar = input()

