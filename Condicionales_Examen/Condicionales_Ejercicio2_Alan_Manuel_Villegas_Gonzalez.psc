//Autor: Alan Manuel Villegas Gonzalez
//UTNG - Desarrollo de Software Multiplataforma	
//GDS0513
//22/Noviembre/2022

//Descripción: Propgrama que solicita el nombre y la edad de una persona y
//muestra su nombre y el nivel educativo.

Algoritmo Nivel_Educativo
	Definir nombre, nvl_educativo Como Caracter;
	Definir edad Como Entero;
	
	//Entrada
	Escribir "Ingresa tu nombre: ";
	Leer nombre;
	Escribir "Ingresa tu edad: ";
	leer edad;
	
	//Calculos y validacion
	Si edad >=3 & edad <= 18 Entonces
		Si edad >= 3 & edad <= 5 Entonces
			nvl_educativo <- "Prescolar";
		FinSi
		Si edad >= 6 & edad <= 12 Entonces
			nvl_educativo <- "Primaria";
		FinSi
		Si edad >= 13 & edad <= 15 Entonces
			nvl_educativo <- "Secundaria";
		FinSi
		Si edad >= 16 & edad <= 18 Entonces
			nvl_educativo <- "Bachillerato";
		FinSi
		
		Escribir "Hola ", nombre, ", perteneces al nivel educativo ", nvl_educativo;
	SiNo
		Escribir nombre, " , la edad que ingresaste no corresponde a ningun nivel educativo";
	FinSi
	
	//Salida
	
FinAlgoritmo
