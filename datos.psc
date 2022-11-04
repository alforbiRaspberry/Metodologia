algoritmo datos
definir dato como cadena;
definir text como cadena;
dimension dato[4];
dimension text[4];
definir i como entero;

text[0] <- "Nombre: ";
text[1] <- "Edad: ";
text[2] <- "Telefono: ";
text[3] <- "Email: ";

para i <- 0 hasta 3 hacer 
  escribir "Ingresa tu ", text[i];
  leer dato[i];
finpara

para i <- 0 hasta 3 hacer
  escribir "Tu ", text[i], "es: ", dato[i];
  escribir "";
FinPara
    finalgoritmo
