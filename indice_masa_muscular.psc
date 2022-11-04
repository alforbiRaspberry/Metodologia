//Autor: Alan Manuel Villegas Gonzalez
Proceso indice_masa_corporal
	Definir peso, altura, imc como real;
	
	Escribir "******************************************************************************************";
	Escribir "Programa que calcula el indice de masa corporal a partir de la altura y peso del usuario";
	Escribir "******************************************************************************************";
	
	Escribir "Ingrese su altura en metros: ";
	leer altura;
	Escribir "Ingrese su peso en kilogramos: ";
	leer peso;
	
	imc <- peso / altura ^ 2;
	
	Escribir "Tu Indice de Masa Corporal (IMC) es: ", imc;
FinProceso
