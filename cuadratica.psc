Proceso cuadratica
	Definir a, b, c, x1, x2 como real;
	
	Escribir "*************************************************";
	Escribir "Programa que calcula los valores de una cuadratica";
	Escribir "****************************************************";
	
	Escribir "Ingresa el valor de a: ";
	leer a;
	Escribir "Ingresa el valor de b: ";
	leer b;
	Escribir "Ingresa el valor de c: ";
	leer c;
	
	x1 <- (-b + (b ^ 2 - 4 * a * c) ^ (1/2)) / (2 * a);
	x2 <- (-b - (b ^ 2 - 4 * a * c) ^ (1/2)) / (2 * a);
	
	Escribir "El valor de x1 es: ", x1;
	Escribir "El valor de x2 es: ", x2;
FinProceso
