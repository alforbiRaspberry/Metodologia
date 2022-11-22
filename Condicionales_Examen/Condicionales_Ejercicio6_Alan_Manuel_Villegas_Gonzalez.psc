//Autor: Alan Manuel Villegas Gonzalez
//UTNG - Desarrollo de Software Multiplataforma	
//GDS0513
//22/Noviembre/2022

//Descripción: Programa que calcula el descuento de una compra por buen fin

Proceso El_Buen_Fin
	Definir monto_a_pagar, descuento, total Como Real;
	Definir tipo_pago Como Caracter;
    descuento <- 0;
	total <- 0;
	
	Escribir "Descuento por BUEN FIN pagando a credito o en efectivo";
	Escribir "Ingrese el monto total a pagar: ";
	leer monto_a_pagar;
	Escribir "Ingrese el tipo de pago (credito/efectivo):";
	leer tipo_pago;
	
	Si Minusculas(tipo_pago) == "credito" | Minusculas(tipo_pago) == "crédito" Entonces
		descuento <- (monto_a_pagar * 0.10);
		total <- monto_a_pagar - descuento;
	SiNo
		Si Minusculas(tipo_pago) == "efectivo" Entonces
			descuento <- monto_a_pagar * 0.10;
			total <- monto_a_pagar - descuento;
		sino 
			Si Minusculas(tipo_pago) == "debito" Entonces
				total <- monto_a_pagar;
		    Sino 
				Escribir "Ingrese un metodo de pago valido";
			FinSi
			
		FinSi
	FinSi
	Escribir "El descuento por BUEN FIN es de $", descuento;
	Escribir "El monto total a pagar es de $", total;

FinProceso
