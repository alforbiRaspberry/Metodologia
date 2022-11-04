//Autor: Alan Manuel Villegas Gonzalez
//Grupo: GDS0513
//Fecha: 04 de noviembre de 2022

Proceso calificacionFinal
	definir ponderacionAsistencia, ponderacionPracticas, ponderacionExamen, calificacion como real;
	
	Escribir "Ingrese el porcentaje obtenido en asistencia: ";
	leer ponderacionAsistencia;
	Escribir "Ingrese el porcentaje obtenido en practicas: ";
	leer ponderacionPracticas;
	Escribir "Ingrese el porcentaje obtenido en el examen: ";
	leer ponderacionExamen;
	
	ponderacionAsistencia <- ponderacionAsistencia * 0.20 / 10;
	ponderacionPracticas <- ponderacionPracticas * 0.30 / 10;
	ponderacionExamen <- ponderacionExamen * 0.50 / 10;
	
	
	calificacion <- ponderacionAsistencia + ponderacionPracticas + ponderacionPracticas;
	Escribir "****************************************************";
	Escribir "Tus ponderaciones son: ";
	Escribir "Asistencia: ", ponderacionAsistencia, " pts.";
	Escribir "Practicas: ", ponderacionPracticas, " pts.";
	Escribir "Examen: ", ponderacionExamen, " pts.";
	Escribir "";
	Escribir "Tu calificación final es: ", calificacion, "/10";
	Escribir "***************************************************";
FinProceso
