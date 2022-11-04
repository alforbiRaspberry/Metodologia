Proceso calcularHipotenusa
	Definir a, b, hipotenusa como real;
	
	Escribir "**********************************************************************************";
	Escribir "Programa que calcula la hipotenusa de un triangulo a partir de los catetos A y B";
	Escribir "**********************************************************************************";
	
	Escribir "Ingrese el cateto a: ";
	leer a;
	Escribir "Ingrese el cateto b: ";
	leer b;
	
	hipotenusa <- (a ^ 2 + b ^ 2) ^ (1 / 2);
	
	Escribir "La hipotenusa de un triangulo con una medida en el cateto a de: ", a;
	Escribir "y una medida en el cateto b de: ", b, " es de: ", hipotenusa;
	
FinProceso
