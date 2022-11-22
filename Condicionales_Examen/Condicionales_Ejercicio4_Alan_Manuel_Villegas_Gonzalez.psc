//Autor: Alan Manuel Villegas Gonzalez
//UTNG - Desarrollo de Software Multiplataforma	
//GDS0513
//22/Noviembre/2022

//Descripción: Programa que dado el nombre de una región indica el
//nombre de los estados que pertenecen a dicha región.

Algoritmo Regiones_de_Mexico
	Definir region Como Caracter;
	
	//Entrada
	Escribir "Programa que muestra los estados de la república según la región ingresada.";
	Escribir "Resiones: Norte, Norte-Occidente, Centro-Norte, Centro, Sur.";
	Escribir "Ingresa la region: ";
	Leer region;
	
	//Calculos, validación y resultados
	Si region == "Norte" | region == "norte" | region == "NORTE" Entonces
		Escribir "Los estados que pertenecen a la region Norte son: ";
		Escribir "Baja California, Sonora, Chihuahua, Coahuila,";
		Escribir "Nuevo León y Tamaulipas.";
	Sino Si region == "Norte-Occidente" | region == "norte-occidente" | region == "NORTE-OCCIDENTE" Entonces
			Escribir "Los estados que pertenecen a la region Norte son: ";
			Escribir "Baja California Sur, Sinaloa, Nayarit, ";
			Escribir "Durango y Zacatecas.";
		Sino Si region == "Centro-Norte" | region == "centro-norte" | region == "CENTRO-NORTE" Entonces
				Escribir "Los estados que pertenecen a la region Norte son: ";
				Escribir "Jalisco, Aguascalientes, Colima, ";
				Escribir "Michoacán y San Luis Potosí.";
			Sino Si region == "Centro" | region == "centro" | region == "CENTRO" Entonces
					Escribir "Los estados que pertenecen a la region Norte son: ";
					Escribir "Guanajuato, Querétaro, Hidalgo, Estado de ";
					Escribir "México, Ciudad de México, Morelos, Tlaxcala y Puebla.";
				Sino Si region == "Sur" | region == "sur" | region == "SUR" Entonces
						Escribir "Los estados que pertenecen a la region Norte son: ";
						Escribir "Guerrero, Oaxaca, Chiapas, Veracruz, Tabasco,";
						Escribir "Campeche, Yucatán y Quintana Roo.";
					Sino Escribir "Error, ingrese ua región valida o compruebe que haya escrito de manera correcta la región ingresada.";
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi

FinAlgoritmo
