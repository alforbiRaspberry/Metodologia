#Author: Alan Manuel Villegas Gonzalez
#UTNG
#Desarrollo de Sowftware multiplataforma - GDS0513
#17 November 2022

from random import randrange

def mostrarMenu():
    print("""
    Condicionales Simples:
    1. Valor Absoluto
    2. Venta de llantas
    3. Descuento al azar
    4. Ecuación Cuadrática
    5. Descuento colegiatura
    6. Enganche casa
    
    Condicionales Dobles
    7. Promedio
    8. Descuento en almacen
    9. Salario semanal
    10. Inicia con vocal o consonante
    11. Descuento de artículo
    12. Compra de camisas
    13. Refacciones
    14. Nombre en minúsculas
    
    Condicionales Multiples
    15. Sueldo trabajador
    16. Hospital en crisis
    17. Descripción del día de la semana
    18. Descripción del mes
    19. Números Romanos
    """)
    #Ejercicio 1 - Condicionales simples: Valor absoluto
def valorAbsoluto():
    print("Programa que calcula el valor absoluto de un numero")
    print("Ingrese un valor: ")
    valor = input()
    valor = float(valor)
    #absoluto = (valor ** 2 ) ** (1/2)
    absoluto = valor
    if valor < 0:
        absoluto = valor * -1

    print("El valor absoluto de ", valor, " es ", absoluto)

#Ejercicio 2 - Condicionales simples: Venta de llantas
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

#Ejercicio 3 - Condicionales simples: Descuento numero al azar
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

#Ejercicio 4 - Condicionales simples: Ecuacion cuadrarica
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

#Ejercicio 5 - Condicionales simples: Descuento colegiatura
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

#Ejercicio 6 - Condicionales Simples: Enganche casa

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

#Ejercicio 1 - Condicionales dobles: Promedio

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

#Ejercicio 2 - Condicionales dobles: Precio de producto en almacén

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


#Ejercicio 3 - Condicionales dobles: Salario Semanal

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

#Ejercicio 4 - Condicionales dobles: Inicia con Vocal

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

#Ejercicio 5 - Condicionales dobles: Descuento Articulo
def descuentoArticulo():
    print("Ingrese el nombre del artículo:")
    nombreArticulo = input()
    print("Ingrese la clave del artículo:")
    clave = int(input())
    print("Ingrese el precio del artículo:")
    precio = float(input())

    if nombreArticulo != None and len(nombreArticulo) >= 3 and len(nombreArticulo) <= 30:
        if clave >= 1 and clave <= 3:
            if clave == 1:
                precioFinal = precio - (precio * .10)
            if clave == 2:
                precioFinal = precio - (precio * .20)
            if clave == 3:
                precioFinal = precio - (precio * .30)
            print("Nombre del artículo:", nombreArticulo)
            print("Clave del artículo:", clave)
            print("Precio original del artículo:", precio)
        else:
            print("Solo se admiten las claves 01, 02 y 03.")
    else:
        print("La longitud del nombre del artículo es incorrecta [3-30].")

# Ejercicio 6 - Condicionales dobles: Compra de camisas
def compraCamisas():
    print("Algoritmo que calcula el precio total a pagar en base a la compra de camisas")
    print("Menos de tres camisas 10% de descuento")
    print("Tres o más 20% de descuento.")
    print("**********************************************************************************")
    print("Ingrese el número de camisas a comprar:")
    numeroCamisas = int(input())
    print("Ingrese el precio de la camisa")
    precioCamisa = float(input())

    if numeroCamisas != None and precioCamisa != None:
        if numeroCamisas > 0 and precio > 0:
            if numeroCamisas >= 3:
                descuento = precioCamisa * .20
            else:
                descuento = precioCamisa * .10
            total = precioCamisa - descuento
            print("Por la compra de", numeroCamisas, " camisas")
            print("Descuento por compra:", descuento)
            print("Total a pagar:", total)
        else:
            print("Error. El programa no acepta números negativos")
    else:
        print("Error. Se ingresaron datos vacíos")

# Ejercicio 7 - Condicionales dobles: Refacciones
def refacciones():
    print("Algoritmo que calcula el total de inversión, préstamo")
    print("y credito que una empresa de refacciones debe solicitar")
    print("**********************************************************")
    print("Ingrese el costo de la pieza:")
    costoPieza = float(input())
    print("Ingrese el numero de piezas a comprar:")
    numeroPiezas = int(input())

    if costoPieza != None and numeroPiezas != None and costoPieza > 0 and numeroPiezas > 0: #Validando que
        totalCompra = numeroPiezas * costoPieza
        if totalCompra >  500000:                                                           #No sean valores
            gastoCapital = totalCompra * .55                                                #Nulos o negativos
            prestamo = totalCompra * .30
            credito = totalCompra * .15
            interes = credito * .20
        else:
            gastoCapital = totalCompra * .70
            prestamo = 0
            credito = totalCompra * .30
            interes = credito * .20
        print("Total de la compra:", totalCompra)
        print("Cantidad inverida:", gastoCapital)
        print("Prestamo:", prestamo)
        print("Credito:", credito)
        print("Interés:", interes)
    else:
        print("Error. No se aceptan valores vacíos o negativos")

# Ejercicio 8 - Condicionales Dobles: Inicia en Minúsculas
def iniciaMinusculas():
    print("Algoritmo que indica si la cadena ingresada inicia con minúsculas")
    print("*******************************************************************")
    print("Ingresa un texto:")
    texto = input()

    if ord(texto[0]) >= 65 and ord(texto[0]) <= 90:
        print("El texto inicia con Mayúsculas")
    elif ord(texto[0]) >= 97 and ord(texto[0]) <= 122:
        print("El texto inicia con Minúsculas")
    else:
        print("El texto no inicia con un letra.")

# Ejercicio 1 - Condicionales multiples- Sueldo Trabajador
def sueldoTrabajador():
    print("Programa que calcula el nuevo salario de un trabajador")
    print("a partir del tipo de trabajador[1-4] y el numero de hijos[1-10]")
    print("*****************************************************************")
    print("                     Tipo de Trabajador                          ")
    print("         1 -------------------------------- 10%                  ")
    print("         2 -------------------------------- 15%                  ")
    print("         3 -------------------------------- 20%                  ")
    print("         4 -------------------------------- 30%                  ")
    print("       Prima de acuerdo al numero de hijos [1-10]                ")
    print("                                                                 ")
    print("*****************************************************************")
    print("Ingresa tu nombre:")
    nombre = input()
    print("Ingresa el tipo de trabajador:")
    tipoTrabajador = int(input())
    print("Ingresa la cantidad de hijos que tienes:")
    numeroHijos = int(input())
    print("Ingresa tu sueldo actual:")
    sueldo = float(input())

    if nombre != None and len(nombre) > 3:  #valida que no haya valores nulos o negativos en el nombre
        if tipoTrabajador != None and tipoTrabajador >= 0 and tipoTrabajador <= 4:  #valida que no haya valores nulos o negativos en el tipo
            if numeroHijos != None and numeroHijos >= 0:    #valida que no haya valores nulos o negativos en el numero de hijos
                if sueldo != None and sueldo > 0:   #valida que no haya valores nulos o negativos en el sueldo
                    if tipoTrabajador == 1:
                        aumento = sueldo * .10
                    elif tipoTrabajador == 2:
                        aumento = sueldo * .15
                    elif tipoTrabajador == 3:
                        aumento = sueldo * .20
                    else:
                        aumento = sueldo * .30
                    primaSueldo = numeroHijos * .05 * sueldo
                    nuevoSueldo = sueldo + aumento + primaSueldo
                    print("Nombre del trabajador:", nombre)
                    print("El tipo de trabajador es", tipoTrabajador, " y el aumento: $", aumento)
                    print("La prima de acuerdo al número de hijos es $", primaSueldo)
                    print("El nuevo sueldo es $", nuevoSueldo)
                else:
                    print("El sueldo ingresado está fuera del rango")
            else:
                print("El numero de hijos no está dentro del rango")
        else:
            print("El tipo de trabajador está fuera del rango")
    else:
        print("El nombre no cumple con los requisitos [3-100]")

# Ejercicio 2 - Condicionales multiples: Hospital En Crisis
def hospitalCrisis():
    print("Programa que calcula el costo total de una estancia en hospital")
    print("dependiendo del tipo de enfermedad y el numero de días en estancia")
    print("*********************************************************************")
    print("                 Tipo de enfermedad a diagnosticar                   ")
    print("         Tipo 1 ------------------------------------- $1500.0        ")
    print("         Tipo 2 ------------------------------------- $1700.0        ")
    print("         Tipo 3 ------------------------------------- $1900.0        ")
    print("                                                                     ")
    print("*********************************************************************")

    nombrePaciente = input("Ingrese el nombre del paciente:")
    tipoEnfermedad = int(input("Ingrese el tipo de enfermedad:"))
    diasEstancia = int(input("Ingrese el numero de días en estancia:"))
    print("\n___________________________________________________________________")

    if nombrePaciente != None and len(nombrePaciente) > 3:
        if tipoEnfermedad != None and tipoEnfermedad > 0 and tipoEnfermedad <= 3:
            if diasEstancia != None and diasEstancia > 0:
                if tipoEnfermedad == 1:
                    costoTotal = diasEstancia * 1500
                elif tipoEnfermedad == 2:
                    costoTotal = diasEstancia * 1700
                else:
                    costoTotal = diasEstancia * 1900
                print("Nombre del paciente:", nombrePaciente)
                print("Días hospitalizado:", diasEstancia)
                print("Tipo de enfermedad:", tipoEnfermedad)
                print("Costo total a pagar:", costoTotal)
            else:
                print("Error. Los días de estancia ingresados están fuera del rango")
        else:
            print("Error. El tipo de enfermedad ingresado está fuera del rango [1-3]")
    else:
        print("Error. El nombre ingresado está fuera del rango [3-100]")

# Ejercicio 3 - Condicionales multiples: Descripción del día de la semana
def diaSemana():
    print("Programa que te da una breve descripción del día de la semana")
    print("*************************************************************")
    print("""
                |   1   |   Domingo     |
                |   2   |   Lunes       |
                |   3   |   Martes      |
                |   4   |   Miércoles   |
                |   5   |   Jueves      |
                |   6   |   Viernes     |
                |   7   |   Sábado      |
*************************************************************
    """)
    dia = int(input("Ingresa el número del día:"))

    if dia != None and dia > 0 and dia < 8:
        if dia == 1:
            print("DOMINGO DIA FELIZ Y DEL SOL")
        elif dia == 2:
            print("LUNES DIA DE LA LUNA")
        elif dia == 3:
            print("MARTES DIA DE MARTE")
        elif dia == 4:
            print("MIERCOLES DIA DE MERCURIO")
        elif dia == 5:
            print("JUEVES DIA DE JUPITER")
        elif dia == 6:
            print("VIERNES DIA DE VENUS")
        else:
            print("SABADO DIA DE SATURNO")
    else:
        print("Error. El número de día ingresado está fuera del rango.")

# Ejercicio 4 - Condicionales multiples: Descripción del mes
def descripcionMeses():
    print("Programa que despliega información del mes")
    print("________________________________________________________________")
    print("""
                    |   1    |   Enero           |
                    |   2    |   Febrero         |
                    |   3    |   Marzo           |
                    |   4    |   Abril           |
                    |   5    |   Mayo            |
                    |   6    |   Junio           |
                    |   7    |   Julio           |
                    |   8    |   Agosto          |
                    |   9    |   Septiembre      |
                    |   10   |   Octubre         |
                    |   11   |   Noviembre       |
                    |   12   |   Diciembre       |
                    |   12   |   Miércoles       |

    ________________________________________________________________
        """)
    mes = int(input("Ingresa el número del día:"))

    if mes != None and mes >= 1 and mes <= 12:
        if mes == 1:
            print("Enero es el primer mes del año en el calendario gregoriano y tiene 31 días.")
        elif mes == 2:
            print("Febrero es el segundo mes del año en el calendario gregoriano. Tiene 28 días y")
            print("29 en los años bisiestos.")
        elif mes == 3:
            print("Marzo es el tercer mes del año en el calendario gregoriano y tiene 31 días.")
        elif mes == 4:
            print("Abril es el cuarto mes del año y es uno de los cuatro meses que tienen 30 días.")
        elif mes == 5:
            print("Mayo es el quinto mes del año en el calendario gregoriano y tiene 31 días.")
        elif mes == 6:
            print("Junio es el sexto mes del año en el Calendario Gregoriano y tiene 30 días.")
        elif mes == 7:
            print("Julio es el séptimo mes del año en el calendario gregoriano y tiene 31 días.")
        elif mes == 8:
            print("Agosto es el octavo mes del año en el calendario gregoriano y tiene 31 días.")
        elif mes == 9:
            print("Septiembre es el noveno mes del año en el calendario gregoriano y tiene 30 días")
        elif mes == 10:
            print("Octubre es el décimo mes del año en el calendario gregoriano y tiene 31 días.")
        elif mes == 11:
            print("Noviembre es el undécimo y penúltimo mes del año en el calendario gregoriano")
            print("y tiene 30 días")
        else:
            print("Diciembre es el duodécimo y último mes del año en el calendario gregoriano y")
            print("tiene 31 días")
    else:
        print("Error. El número de mes ingresado está fuera del rango.")

# Ejercicio 5 - Condicionales Multiples: Números romanos
def numerosRomanos():
    print("*******************************************************************************")
    print("Algoritmo que calcula la equivalencia de un número ingresado a número romano")
    print("*******************************************************************************")
    numero = int(input("Ingresa un numero entero entre 1 y 100: "))

    if numero != None and numero > 0 and numero <= 100:
        decenas = 0
        for i in range (1, numero+1):
            if i % 10 == 0:
                decenas += 1
        unidades = numero - decenas * 10
        unidadesRomanas = ""
        decenasRomanos = ""
        if decenas == 1:
            decenasRomanos = 'X'
        elif decenas == 2:
            decenasRomanos = "XX"
        elif decenas == 3:
            decenasRomanos = "XXX"
        elif decenas == 4:
            decenasRomanos = "XL"
        elif decenas == 5:
            decenasRomanos = "L"
        elif decenas == 6:
            decenasRomanos = "LX"
        elif decenas == 7:
            decenasRomanos = "LXX"
        elif decenas == 8:
            decenasRomanos = "LXXX"
        elif decenas == 9:
            decenasRomanos = "XC"
        elif decenas == 10:
            decenasRomanos = "C"
        if unidades == 1:
            unidadesRomanas = 'I'
        elif unidades == 2:
            unidadesRomanas = "II"
        elif unidades == 3:
            unidadesRomanas = "III"
        elif unidades == 4:
            unidadesRomanas = "IV"
        elif unidades == 5:
            unidadesRomanas = "V"
        elif unidades == 6:
            unidadesRomanas = "VI"
        elif unidades == 7:
            unidadesRomanas = "VII"
        elif unidades == 8:
            unidadesRomanas = "XIII"
        elif unidades == 9:
            unidadesRomanas = "IX"
        print("El numero", numero, " en romano es:", decenasRomanos + unidadesRomanas)
    else:
        print("Error. El número ingresado está fuera del rango [1-100]")




#Main del programa
opcion = 0
continuar = 'y'
while continuar != 'n':
    print("*******************************************")
    print("  Ingrese el programa que desee ejecutar. Presione 0 para mostrar las opciones[1-19]")
    opcion = input()
    opcion = int(opcion)
    while opcion == 0:
        mostrarMenu()
        print("  Ingrese el programa que desee ejecutar. Presione 0 para mostrar las opciones [1-19]")
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
    elif opcion == 11:
        descuentoArticulo()
    elif opcion == 12:
        compraCamisas()
    elif opcion == 13:
        refacciones()
    elif opcion == 14:
        iniciaMinusculas()
    elif opcion == 15:
        sueldoTrabajador()
    elif opcion == 16:
        hospitalCrisis()
    elif opcion == 17:
        diaSemana()
    elif opcion == 18:
        descripcionMeses()
    elif opcion == 19:
        numerosRomanos()
    else :
        print("Opción no valida. Intente de nuevo.")
    print("Desea ejecutar otro programa? (y/n): ")
    continuar = input()

