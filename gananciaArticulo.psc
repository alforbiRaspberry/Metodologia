//Autor: Alan Manuel Villegas Gonzalez

Proceso tienda_auto_servicio 
	definir precioArticulo, gananciaArticulo como real;
	
	Escribir "************************************";
	Escribir "La ganancia del articulo es del 30%";
	Escribir "************************************";
	
	Escribir "Ingrese el precio del articulo: ";
	leer precioArticulo;
	
	gananciaArticulo <- precioArticulo * 0.30;
	
	Escribir "La ganancia del articulo con precio $", precioArticulo, " es de: ", gananciaArticulo;
FinProceso
