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

#Ejercicio 6 - Condicionales Simples

def engancheCasa():
    print("Programa que calcula el enganche de una casa y el monto mensual a pagar")
    print ("Si el ingreso es mayor a $8000 el enganche es del 15% a pagar en 5 años")
    print("Si el ingreso es menor a $4000 el enganche es del 25% a pagar a 10 años")


    print("Ingresa tu salario mensual: ")
    salario = float(input())

    print("Ingresa el costo de la casa: ")
    costo_casa = float(input())
    pago_mensual = 0
    enganche = 0

    if salario <= 0 or costo_casa <= 0:
        print("Error. Asegurate de no ingresar numeros negativos")
    if salario >= 4000 and salario < 8000:
        enganche = costo_casa * 0.25
        pago_mensual = (costo_casa - enganche) / 120
        print("El enganche es de $", enganche)
        print("Los pagos a realizar son de $", pago_mensual, " a 10 años")
    if salario > 8000:
        enganche = costo_casa * 0.15
        pago_mensual = (costo_casa - enganche) / 60
        print("El enganche es de $", enganche)
        print("Los pagos a realizar son de $", pago_mensual, " a 5 años")
    if salario > 0:
        print ("El ingreso no es suficiente para adquirir una casa")

#Ejercicio 1 - Condicionales dobles

def promedio():
    print("Programa que determina si un alumnmo aprueba o reprueba el curso en base a las ")
    print("calificaciones de cada unidad")
    print("la calificacion minima aprobatoria es de 8")

    validacion = 1
    sumatoria = 0
    print("Ingrese la calificacion de la unidad 1: ")
    aux = float(input())
    if aux < 0:
        validacion = 0
    sumatoria += aux
    print("Ingrese la calificacion de la unidad 2: ")
    aux = float(input())
    if aux < 0:
        validacion = 0
    sumatoria += aux
    print("Ingrese la calificacion de la unidad 3: ")
    aux = float(input())
    if aux < 0:
        validacion = 0
    sumatoria += aux

    promedio = sumatoria / 3

    if validacion == 1:
        if promedio >= 8:
            print("El alumno aprobó. Calificación final: ", promedio)
        else:
            print("El alumno no aprobó. Calificación: ", promedio)
    else:
        print("Error en la toma de datos. Asegurese de no ingresar valores negativos")

#Ejercicio 2 - Condicionales dobles

def precioProductoAlmacen():
    print("Programa que calcula el descuento de una compra de almacén")
    print("Se aplicará un descuento del 20% si la compra es mayor o igual a 2000")
    print("Ingrese el monto de la compra: ")
    monto = float(input())

    if monto > 0:
        if monto >= 1000:
            descuento = monto * 0.20
            monto += descuento
            print("El descuento es de $", descuento)
            print("Total a pagar $", monto)
        else:
            print("No hay descuento.")
            print("El total a pagar es $", monto)
    else:
        print("El monto ", monto, " no es valido.")


#Ejercicio 3 - Condicionales dobles

def salarioSemanal():
    print ("Programa para calcular el salario semanal de un trabajador")
    print("Un obrero de manera normal trabaja 40 horas")
    print("La hora se oaga a $16 y la extra a $32")
    print("Ingrese las horas trabajadas por el obrero: ")
    horas_trabajadas = int(input())

    if horas_trabajadas < 0:
        print("Error en la toma de datos, asegurate de no introducir ")
        print("valores negativos")
    else:
        if horas_trabajadas > 40:
            salario = 40 * 16 + (horas_trabajadas - 40) * 32 #horas_trabajadas - 40 se refiere a las horas extra
            print("Se trabajaron ", horas_trabajadas, " horas")
            print("Por ", horas_trabajadas - 40, " horas extra el pago es $", (horas_trabajadas - 40) * 32)
            print("Más el pago de 40 horas $", horas_trabajadas * 16)
            print("El salario final es", salario)
        else:
            salario = horas_trabajadas * 16
            print("Se trabajaron ", horas_trabajadas, " horas")
            print("No hubo horas extra")
            print("El total a pagar es $", salario)

#Ejercicio 4 - Condicionales dobles

def iniciaVocal():
    print("Programa que indica si el nombre ingresado inicia con vocal o consonante")
    print("Ingrese el nombre: ")
    nombre = input()

    if len(nombre) >= 3 and len(nombre) <= 30:
        nombre_lower = str.lower(nombre)
        if nombre_lower[0] == "a" or nombre_lower[0] == "e" or nombre_lower[0] == "i" or nombre_lower[0] == "o" or nombre_lower[0] == "u":
            print(nombre, " empieza con vocal", str.upper(nombre[0]))
        else:
            print(nombre, "empieza con consonante", str.upper(nombre[0]))
    else:
        print("La longitud de la cadena no es la correcta [3-30]")

#Ejercicio 5 - Condicionales dobles

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
    elif opcion == 5:
        pagoColegiatura()
    elif opcion == 6:
        engancheCasa()
    elif opcion == 7:
        promedio()
    elif opcion == 8:
        precioProductoAlmacen()
    elif opcion == 9:
        salarioSemanal()
    elif opcion == 10:
        iniciaVocal()
    else :
        print("Opción no valida. Intente de nuevo.")
    print("Desea ejecutar otro programa? (y/n): ")
    continuar = input()

