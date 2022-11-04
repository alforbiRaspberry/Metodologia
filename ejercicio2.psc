//Autor: Alan Manuel Villegas Gonzalez
//Grupo: GDS0513
//Fecha: 04 de noviembre de 2022

Proceso descuentoPagoFinal
	
	Definir costoColegiatura, descuento, costoDefinitivo como real;
	
	Escribir "******************************";
	Escribir "*******Sistema de promocion**********";
	Escribir "******************************";
	Escribir "Por ser fin de año, se aplicará un descuento del 25%";
	Escribir "Ingrese la cantidad de la colegiatura para aplicar el descuento: ";
	leer costoColegiatura;
	descuento <- costoColegiatura * 0.25;
	costoDefinitivo <- costoColegiatura - descuento;
	
	Escribir "El descuento para una colegiatura de $ ", costoColegiatura, " es de: $", descuento;
	Escribir "El costo final de la colegiatura es de: $", costoDefinitivo;
	
FinProceso
