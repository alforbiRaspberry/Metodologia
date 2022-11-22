//Autor: Alan Manuel Villegas Gonzalez
//UTNG - Desarrollo de Software Multiplataforma	
//GDS0513
//22/Noviembre/2022

//Descripción: Programa que calcula la conversion de temperaturas
Proceso Conversor_Temperatura
	
	Definir grados_resultado, grados Como Real;
	Definir opcion como Entero;
	
	Escribir"Menú";
	Escribir"[1] Convertir de ºC a ºF";
	Escribir"[2] convertir de ºF a ºC";
	Escribir"[3] convertir de ºC a ºK";
	Escribir"[4] convertir de ºK a ºC";
	Escribir"[5] convertir de ºK a ºF";
	Escribir"[6] convertir de ºF a ºK";
	
	Escribir "Seleccione la opción: ";
	leer opcion;
	Escribir "Ingrese los grados: ";
	leer grados;
	
	Si opcion >= 1 | opcion <= 6 Entonces 
		si opcion == 1 Entonces
			grados_resultado <- grados * 1.8 + 32;
			Escribir grados, " °C equivalen a ", grados_resultado, " °F";
		FinSi
		si opcion == 2 Entonces
			grados_resultado <- (grados - 32) / 18;
			Escribir grados, " °F equivalen a ", grados_resultado, " °C";
		FinSi
		si opcion == 3 Entonces
			grados_resultado <- grados - 273.15;
			Escribir grados, " °C equivalen a ", grados_resultado, " °K";
		FinSi
		si opcion == 4 Entonces
			grados_resultado <- grados + 273.15;
			Escribir grados, " °K equivalen a ", grados_resultado, " °C";
		FinSi
		si opcion == 5 Entonces
			grados_resultado <- 5/9 * (grados - 32) + 273.15;
			Escribir grados, " °K equivalen a ", grados_resultado, " °F";
		FinSi
		si opcion == 6 Entonces
			grados_resultado <- 1.8 * (grados - 273.15) + 32;
			Escribir grados, " °F equivalen a ", grados_resultado, " °K";
		FinSi
	SiNo
		Escribir "Ingrese una opcion valida.";
	FinSi
FinProceso
